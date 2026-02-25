# 跨頻率資料存取模式

## 問題：中間變數覆蓋

當主頻率為分鐘 K 時，若將跨頻率資料存入變數，
該變數會在**每個 tick 都被主頻率覆蓋**，導致值不正確。

### 錯誤寫法

```xs
// 主頻率：5 分 K
var: _DailyClose(0);
var: _DailyMA(0);

// 錯誤！這些變數會被每個 5 分 tick 覆蓋
_DailyClose = GetField("收盤價", "D");
_DailyMA = Average(_DailyClose, 20);  // 不是日線的 20MA！

if Close > _DailyMA then
    plot1(1, "訊號");
```

### 正確寫法：直接使用 GetField

```xs
// 正確：不存中間變數，直接使用
if Close > Average(GetField("收盤價", "D"), 20) then
    plot1(1, "訊號");
```

## xf_ 與 xfMin_ 系列函數

XS 提供跨頻率輔助函數，直接在目標頻率上計算：

### xf_ 系列（日 K 以上頻率）

```xs
// xf_Average: 在日線頻率上計算均線
value1 = xf_Average("D", Close, 20);

// xf_Highest: 在週線頻率上取最高
value2 = xf_Highest("W", High, 10);

// xf_RSI: 在日線上算 RSI
value3 = xf_RSI("D", Close, 14);
```

### xfMin_ 系列（分鐘頻率）

```xs
// xfMin_Average: 在 60 分 K 上計算均線
value1 = xfMin_Average(60, Close, 20);

// xfMin_Highest: 在 30 分 K 上取最高
value2 = xfMin_Highest(30, High, 10);
```

## 正確的跨頻率比較範例

```xs
// 在 5 分 K 圖上，比較日線 MA 和週線 MA
input: _FastPeriod(5, "日線均線期數");
input: _SlowPeriod(10, "週線均線期數");

var: _Signal(0);

// 直接用 xf_ 計算，不存中間變數
if xf_Average("D", Close, _FastPeriod) > xf_Average("W", Close, _SlowPeriod) then
    _Signal = 1
else
    _Signal = -1;

plot1(_Signal, "多空方向");
```

## 規則總結
1. **不要**將 GetField 跨頻率結果存入 var 變數
2. **直接**在條件判斷中使用 GetField 或 xf_ 函數
3. 分鐘級跨頻率用 `xfMin_`，日級以上用 `xf_`
4. 若需要多次引用同一跨頻率值，重複呼叫 GetField 即可（XQ 內部有快取）
