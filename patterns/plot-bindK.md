# Plot 與 PlotK 互斥規則

## 兩種繪圖方式

### plot 系列：畫數值線
```xs
plot1(數值, "名稱");
plot2(數值, "名稱", 是否預設勾選);
```

### PlotK：畫 K 棒
```xs
PlotK(序列編號, 開盤, 最高, 最低, 收盤, "名稱");
```

## 核心規則：不能混用

**同一個腳本中，plot 和 PlotK 不能同時使用。**

```xs
// 錯誤：混用 plot 和 PlotK
plot1(_MA, "均線");
PlotK(1, Open, High, Low, Close, "K棒");  // 衝突！
```

## plot 正確用法

```xs
input: _Fast(5, "快線週期");
input: _Slow(20, "慢線週期");

var: _FastMA(0);
var: _SlowMA(0);

_FastMA = Average(Close, _Fast);
_SlowMA = Average(Close, _Slow);

// plot 只指定值和名稱，不能指定顏色/樣式/寬度
plot1(_FastMA, "快線");
plot2(_SlowMA, "慢線");
plot3(0, "零軸", true);  // true = 預設勾選顯示
```

- `plot1` ~ `plot99` 可用
- 第三個參數為 boolean，控制是否預設勾選
- **顏色、線型、寬度由使用者在 XQ 介面設定**，腳本無法控制

## PlotK 正確用法

```xs
// 畫 Heikin-Ashi K 棒
var: _haClose(0);
var: _haOpen(0);
var: _haHigh(0);
var: _haLow(0);

_haClose = (Open + High + Low + Close) / 4;
_haOpen = (_haOpen[1] + _haClose[1]) / 2;
_haHigh = Highest(High, 1);
_haLow = Lowest(Low, 1);

PlotK(1, _haOpen, _haHigh, _haLow, _haClose, "HA K棒");
```

- `PlotK` 的第一個參數是序列編號（1, 2, 3...）
- 可畫多組 K 棒（不同序列編號）
- 同樣**無法在腳本中控制顏色**

## PlotK 畫跨頻率 K 棒

```xs
// 在分鐘圖上疊加日 K 棒
PlotK(1,
    GetField("開盤價", "D"),
    GetField("最高價", "D"),
    GetField("最低價", "D"),
    GetField("收盤價", "D"),
    "日K");
```

## 決策指引
| 需求 | 使用 |
|------|------|
| 畫均線、指標值 | plot |
| 畫自訂 K 棒 | PlotK |
| 畫指標 + K 棒 | **拆成兩個腳本** |
