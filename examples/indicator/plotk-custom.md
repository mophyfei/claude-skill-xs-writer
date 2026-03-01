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
// 使用頻率參數 "還原日" 取得還原價格
variable: _adjOpen(0), _adjHigh(0), _adjLow(0), _adjClose(0);

_adjOpen = GetField("開盤價", "還原日");
_adjHigh = GetField("最高價", "還原日");
_adjLow = GetField("最低價", "還原日");
_adjClose = GetField("收盤價", "還原日");

PlotK(_adjOpen, _adjHigh, _adjLow, _adjClose, "還原K線");
```

## Heikin-Ashi K線

```xs
// 平均K線 (Heikin-Ashi)
variable: _haOpen(0), _haClose(0), _haHigh(0), _haLow(0);

// HA收盤 = (開+高+低+收)/4
_haClose = (Open + High + Low + Close) / 4;

// HA開盤 = 前根HA開盤和HA收盤的平均
if CurrentBar = 1 then
  _haOpen = (Open + Close) / 2
else
  _haOpen = (_haOpen[1] + _haClose[1]) / 2;

// HA最高 = Max(High, haOpen, haClose)
_haHigh = MaxList(High, _haOpen, _haClose);

// HA最低 = Min(Low, haOpen, haClose)
_haLow = MinList(Low, _haOpen, _haClose);

PlotK(_haOpen, _haHigh, _haLow, _haClose, "HA K線");
```

## 週K線（日線圖上顯示週K）

```xs
// 在日線圖上繪製週K線
variable: _wOpen(0), _wHigh(0), _wLow(0), _wClose(0);
variable: _isNewWeek(false);

// 判斷是否為新的一週（週一或本週第一個交易日）
_isNewWeek = DayOfWeek(Date) < DayOfWeek(Date[1]);

if _isNewWeek then begin
  _wOpen = Open;
  _wHigh = High;
  _wLow = Low;
end
else begin
  if High > _wHigh then _wHigh = High;
  if Low < _wLow then _wLow = Low;
end;
_wClose = Close;

PlotK(_wOpen, _wHigh, _wLow, _wClose, "週K");
```

## PlotK 搭配條件變色

```xs
// K線依據成交量變色
// 注意：PlotK 的顏色需透過 SetPlotColor 設定
variable: _avgVol(0);

_avgVol = Average(Volume, 20);

PlotK(Open, High, Low, Close, "量能K線");

// 量大於均量2倍時變色
if Volume > _avgVol * 2 then
  SetPlotColor(1, "Red")
else if Volume > _avgVol then
  SetPlotColor(1, "Yellow")
else
  SetPlotColor(1, "White");
```
