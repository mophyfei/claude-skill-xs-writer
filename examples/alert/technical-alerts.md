# 警示範例：技術面警示

## 均線黃金交叉警示

```xs
// 5日均線穿越20日均線
variable: ma5(0), ma20(0);

ma5 = Average(Close, 5);
ma20 = Average(Close, 20);

// 黃金交叉
if ma5 Cross Over ma20 then
  ret = 1;
```

## 均線死亡交叉警示

```xs
// 5日均線跌破20日均線
variable: ma5(0), ma20(0);

ma5 = Average(Close, 5);
ma20 = Average(Close, 20);

// 死亡交叉
if ma5 Cross Under ma20 then
  ret = 1;
```

## 爆量警示

```xs
// 成交量突然放大
variable: avgVol(0);

avgVol = Average(Volume, 20);

// 成交量超過20日均量的3倍
if Volume > avgVol * 3 then
  ret = 1;
```

## 突破前高警示

```xs
// 股價突破近60日新高
variable: prevHigh(0);

prevHigh = Highest(High, 60)[1];  // 前60日最高（不含今日）

if Close > prevHigh then
  ret = 1;
```

## 跌破前低警示

```xs
// 股價跌破近20日新低
variable: prevLow(0);

prevLow = Lowest(Low, 20)[1];  // 前20日最低（不含今日）

if Close < prevLow then
  ret = 1;
```

## RSI 超買超賣警示

```xs
// RSI進入極端區域
variable: rsiVal(0);

rsiVal = RSI(Close, 14);

// RSI < 20 極度超賣
if rsiVal Cross Under 20 then
  ret = 1;

// 也可以警示超買：rsiVal Cross Over 80
```

## MACD 交叉警示

```xs
// MACD線穿越信號線
variable: macdLine(0), signalLine(0);

macdLine = XAverage(Close, 12) - XAverage(Close, 26);
signalLine = XAverage(macdLine, 9);

// MACD黃金交叉（零軸以下更有意義）
if macdLine Cross Over signalLine
   AND macdLine < 0  // 在零軸下方交叉
then ret = 1;
```

## 布林通道突破警示

```xs
// 收盤突破布林上軌
variable: midBand(0), upperBand(0);

midBand = Average(Close, 20);
upperBand = midBand + 2 * StandardDev(Close, 20);

if Close Cross Over upperBand then
  ret = 1;
```

## KD 低檔交叉警示

```xs
// KD在低檔區交叉
variable: rsv(0), kVal(0), dVal(0);

rsv = (Close - Lowest(Low, 9)) / (Highest(High, 9) - Lowest(Low, 9)) * 100;
kVal = XAverage(rsv, 3);
dVal = XAverage(kVal, 3);

if kVal Cross Over dVal AND kVal < 25 then
  ret = 1;
```

## 跳空缺口警示

```xs
// 向上跳空缺口
if Low > High[1] then    // 今低 > 昨高 = 向上跳空
  ret = 1;

// 向下跳空可改為：High < Low[1]
```
