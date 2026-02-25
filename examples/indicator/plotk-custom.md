# 指標範例：PlotK 自訂K線

## 基本 PlotK 用法

```xs
// PlotK 繪製自訂K線圖
// 語法：PlotK(Open, High, Low, Close, "名稱")
// 注意：PlotK 只能出現一次，且不可與 Plot1~99 混用在同一個副圖

// 繪製原始K線
PlotK(Open, High, Low, Close, "原始K線");
```

## 還原K線

```xs
// 繪製除權息還原K線
variable: adjOpen(0), adjHigh(0), adjLow(0), adjClose(0);

adjOpen = GetField("還原開盤價");
adjHigh = GetField("還原最高價");
adjLow = GetField("還原最低價");
adjClose = GetField("還原收盤價");

PlotK(adjOpen, adjHigh, adjLow, adjClose, "還原K線");
```

## Heikin-Ashi K線

```xs
// 平均K線 (Heikin-Ashi)
variable: haOpen(0), haClose(0), haHigh(0), haLow(0);

// HA收盤 = (開+高+低+收)/4
haClose = (Open + High + Low + Close) / 4;

// HA開盤 = 前根HA開盤和HA收盤的平均
if CurrentBar = 1 then
  haOpen = (Open + Close) / 2
else
  haOpen = (haOpen[1] + haClose[1]) / 2;

// HA最高 = Max(High, haOpen, haClose)
haHigh = MaxList(High, haOpen, haClose);

// HA最低 = Min(Low, haOpen, haClose)
haLow = MinList(Low, haOpen, haClose);

PlotK(haOpen, haHigh, haLow, haClose, "HA K線");
```

## 週K線（日線圖上顯示週K）

```xs
// 在日線圖上繪製週K線
variable: wOpen(0), wHigh(0), wLow(0), wClose(0);
variable: isNewWeek(false);

// 判斷是否為新的一週（週一或本週第一個交易日）
isNewWeek = DayOfWeek(Date) < DayOfWeek(Date[1]);

if isNewWeek then begin
  wOpen = Open;
  wHigh = High;
  wLow = Low;
end
else begin
  if High > wHigh then wHigh = High;
  if Low < wLow then wLow = Low;
end;
wClose = Close;

PlotK(wOpen, wHigh, wLow, wClose, "週K");
```

## PlotK 搭配條件變色

```xs
// K線依據成交量變色
// 注意：PlotK 的顏色需透過 SetPlotColor 設定
variable: avgVol(0);

avgVol = Average(Volume, 20);

PlotK(Open, High, Low, Close, "量能K線");

// 量大於均量2倍時變色
if Volume > avgVol * 2 then
  SetPlotColor(1, "Red")
else if Volume > avgVol then
  SetPlotColor(1, "Yellow")
else
  SetPlotColor(1, "White");
```
