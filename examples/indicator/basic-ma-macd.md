# 指標範例：均線 + MACD

## 簡單移動平均線 (SMA)

```xs
// 繪製多條均線
input: period1(5, "短期均線");
input: period2(20, "中期均線");
input: period3(60, "長期均線");

variable: ma5(0), ma20(0), ma60(0);

ma5 = Average(Close, period1);
ma20 = Average(Close, period2);
ma60 = Average(Close, period3);

Plot1(ma5, "MA5");
Plot2(ma20, "MA20");
Plot3(ma60, "MA60");
```

## 均線多頭排列判斷

```xs
// 短>中>長 = 多頭排列
variable: ma5(0), ma20(0), ma60(0);

ma5 = Average(Close, 5);
ma20 = Average(Close, 20);
ma60 = Average(Close, 60);

// 多頭排列
if ma5 > ma20 AND ma20 > ma60 then
  Plot1(1, "多頭排列")
else
  Plot1(0, "多頭排列");
```

## 均線交叉信號

```xs
// 黃金交叉 / 死亡交叉
variable: maShort(0), maLong(0);

maShort = Average(Close, 5);
maLong = Average(Close, 20);

// 黃金交叉：短均線由下向上穿越長均線
if maShort Cross Over maLong then
  Plot1(1, "交叉信號")
// 死亡交叉：短均線由上向下穿越長均線
else if maShort Cross Under maLong then
  Plot1(-1, "交叉信號")
else
  Plot1(0, "交叉信號");
```

## MACD 指標

```xs
// 標準 MACD 指標
input: fastLen(12, "快線週期");
input: slowLen(26, "慢線週期");
input: signalLen(9, "信號線週期");

variable: fastEMA(0), slowEMA(0);
variable: macdLine(0), signalLine(0), histogram(0);

fastEMA = XAverage(Close, fastLen);
slowEMA = XAverage(Close, slowLen);

// MACD線 = 快線 - 慢線
macdLine = fastEMA - slowEMA;
// 信號線 = MACD線的EMA
signalLine = XAverage(macdLine, signalLen);
// 柱狀圖 = MACD線 - 信號線
histogram = macdLine - signalLine;

Plot1(macdLine, "MACD");
Plot2(signalLine, "Signal");
Plot3(histogram, "Histogram");
Plot4(0, "Zero");
```

## MACD 背離偵測

```xs
// 價格創新低但MACD未創新低 = 底背離
variable: macdLine(0);
variable: prevLow(0), prevMACD(0);

macdLine = XAverage(Close, 12) - XAverage(Close, 26);

// 簡易底背離判斷
if Low < Lowest(Low, 20)[1]
   AND macdLine > Lowest(macdLine, 20)[1] then
  Plot1(1, "底背離")
else
  Plot1(0, "底背離");
```
