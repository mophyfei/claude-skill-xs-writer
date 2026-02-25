# 指標範例：布林通道 + ATR

## 布林通道 (Bollinger Bands)

```xs
// 標準布林通道
input: period(20, "均線週期");
input: numStdDev(2, "標準差倍數");

variable: midBand(0), upperBand(0), lowerBand(0);
variable: bandWidth(0), percentB(0);

midBand = Average(Close, period);
upperBand = midBand + numStdDev * StandardDev(Close, period);
lowerBand = midBand - numStdDev * StandardDev(Close, period);

Plot1(upperBand, "上軌");
Plot2(midBand, "中軌");
Plot3(lowerBand, "下軌");
```

## 布林帶寬與 %B

```xs
// 帶寬收斂 = 即將突破的信號
input: period(20, "週期");
input: numStdDev(2, "標準差");

variable: midBand(0), upperBand(0), lowerBand(0);
variable: bandWidth(0), percentB(0);

midBand = Average(Close, period);
upperBand = midBand + numStdDev * StandardDev(Close, period);
lowerBand = midBand - numStdDev * StandardDev(Close, period);

// 帶寬 = (上軌-下軌)/中軌
if midBand <> 0 then
  bandWidth = (upperBand - lowerBand) / midBand * 100;

// %B = (收盤-下軌)/(上軌-下軌)
if (upperBand - lowerBand) <> 0 then
  percentB = (Close - lowerBand) / (upperBand - lowerBand) * 100;

Plot1(bandWidth, "帶寬%");
Plot2(percentB, "%B");
Plot3(80, "超買");
Plot4(20, "超賣");
```

## ATR (Average True Range)

```xs
// 平均真實波幅
input: atrPeriod(14, "ATR週期");

variable: trueRange(0), atrValue(0);

// 真實波幅 = Max(當日高低差, 前收到今高, 前收到今低)
trueRange = TrueRange;

// ATR = 真實波幅的移動平均
atrValue = AvgTrueRange(atrPeriod);

Plot1(atrValue, "ATR");
```

## ATR 通道

```xs
// 基於ATR的動態通道
input: atrPeriod(14, "ATR週期");
input: atrMult(2, "ATR倍數");
input: maPeriod(20, "均線週期");

variable: atrVal(0), maVal(0);
variable: upperCh(0), lowerCh(0);

atrVal = AvgTrueRange(atrPeriod);
maVal = Average(Close, maPeriod);

upperCh = maVal + atrMult * atrVal;
lowerCh = maVal - atrMult * atrVal;

Plot1(upperCh, "ATR上軌");
Plot2(maVal, "均線");
Plot3(lowerCh, "ATR下軌");
```

## ATR 波動率指標

```xs
// 波動率相對高低判斷
input: atrPeriod(14, "ATR週期");
input: lookback(100, "回顧期間");

variable: atrVal(0), atrHigh(0), atrLow(0), atrPct(0);

atrVal = AvgTrueRange(atrPeriod);
atrHigh = Highest(atrVal, lookback);
atrLow = Lowest(atrVal, lookback);

// ATR百分位：0=極低波動, 100=極高波動
if (atrHigh - atrLow) <> 0 then
  atrPct = (atrVal - atrLow) / (atrHigh - atrLow) * 100;

Plot1(atrPct, "ATR百分位");
Plot2(80, "高波動");
Plot3(20, "低波動");
```
