# XS 語法基礎規則

## 命名規則
- 所有 `input` 和 `var` 名稱**必須以 `_` 開頭**
- 範例：`_Period`, `_Price`, `_Flag`

## input 與 var 宣告差異

```xs
// input: 名稱, 預設值, 說明文字
input: _Period(20, "均線週期");
input: _Threshold(0.05, "門檻值(%)");

// var: 只有名稱和初始值，不寫說明
var: _Signal(0);
var: _AvgPrice(0);
```

## 運算子規則
- `=` **同時用於比較和賦值**，沒有 `==`
- 比較不等於使用 `<>`

```xs
// 賦值
_Signal = 1;

// 比較（同樣用 =）
if _Signal = 1 then ...

// 不等於
if _Signal <> 0 then ...
```

## 內建函數優先
- 優先使用 XS 內建函數，不要自行實作已有的邏輯
- 例如用 `Average(Close, _Period)` 而非手動算加總再除

## 序列索引
- 使用 `[]` 存取歷史值：`Close[1]` = 前一根 K 棒收盤價
- `[0]` 等同當前值

## 日期換日判斷
- **禁止**使用 `newday`
- **正確**：`date <> date[1]`

```xs
if date <> date[1] then begin
    _DayHigh = High;
    _DayLow = Low;
end;
```

## 跨頻率資料
- **直接使用 `GetField`**，不要存入中間變數（會被主頻率覆蓋）

```xs
// 正確
if GetField("收盤價", "D") > GetField("收盤價", "D")[1] then ...

// 錯誤：中間變數會被覆蓋
var: _DClose(0);
_DClose = GetField("收盤價", "D");  // 每 tick 都會變
```

## 多週期資料判斷
- **不要使用陣列**來儲存多週期資料
- 直接用 `[]` 索引存取歷史值即可

```xs
// 正確：直接用索引
if Close > Close[1] and Close[1] > Close[2] then ...
```
