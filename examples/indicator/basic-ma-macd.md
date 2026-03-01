# 指標範例：均線 + MACD

## 簡單移動平均線 (SMA)

```xs
// 繪製多條均線
input: _period1(5, "短期均線");
input: _period2(20, "中期均線");
input: _period3(60, "長期均線");

variable: _ma5(0), _ma20(0), _ma60(0);

_ma5 = Average(Close, _period1);
_ma20 = Average(Close, _period2);
_ma60 = Average(Close, _period3);

Plot1(_ma5, "MA5");
Plot2(_ma20, "MA20");
Plot3(_ma60, "MA60");
```

## 均線多頭排列判斷

```xs
// 短>中>長 = 多頭排列
variable: _ma5(0), _ma20(0), _ma60(0);

_ma5 = Average(Close, 5);
_ma20 = Average(Close, 20);
_ma60 = Average(Close, 60);

// 多頭排列
if _ma5 > _ma20 AND _ma20 > _ma60 then
  Plot1(1, "多頭排列")
else
  Plot1(0, "多頭排列");
```

## 均線交叉信號

```xs
// 黃金交叉 / 死亡交叉
variable: _maShort(0), _maLong(0);

_maShort = Average(Close, 5);
_maLong = Average(Close, 20);

// 黃金交叉：短均線由下向上穿越長均線
if _maShort Cross Over _maLong then
  Plot1(1, "交叉信號")
// 死亡交叉：短均線由上向下穿越長均線
else if _maShort Cross Under _maLong then
  Plot1(-1, "交叉信號")
else
  Plot1(0, "交叉信號");
```

## MACD 指標

```xs
// 標準 MACD 指標
input: _fastLen(12, "快線週期");
input: _slowLen(26, "慢線週期");
input: _signalLen(9, "信號線週期");

variable: _fastEMA(0), _slowEMA(0);
variable: _macdLine(0), _signalLine(0), _histogram(0);

_fastEMA = XAverage(Close, _fastLen);
_slowEMA = XAverage(Close, _slowLen);

// MACD線 = 快線 - 慢線
_macdLine = _fastEMA - _slowEMA;
// 信號線 = MACD線的EMA
_signalLine = XAverage(_macdLine, _signalLen);
// 柱狀圖 = MACD線 - 信號線
_histogram = _macdLine - _signalLine;

Plot1(_macdLine, "MACD");
Plot2(_signalLine, "Signal");
Plot3(_histogram, "Histogram");
Plot4(0, "Zero");
```

## MACD 背離偵測

```xs
// 價格創新低但MACD未創新低 = 底背離
variable: _macdLine(0);
variable: _prevLow(0), _prevMACD(0);

_macdLine = XAverage(Close, 12) - XAverage(Close, 26);

// 簡易底背離判斷
if Low < Lowest(Low, 20)[1]
   AND _macdLine > Lowest(_macdLine, 20)[1] then
  Plot1(1, "底背離")
else
  Plot1(0, "底背離");
```
