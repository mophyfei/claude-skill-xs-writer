# 選股範例：技術面

## 均線多頭排列

```xs
// 均線多頭排列選股
variable: ma5(0), ma10(0), ma20(0), ma60(0);

ma5 = Average(Close, 5);
ma10 = Average(Close, 10);
ma20 = Average(Close, 20);
ma60 = Average(Close, 60);

// 短>中>長 = 多頭排列
if ma5 > ma10 AND ma10 > ma20 AND ma20 > ma60
   AND Close > ma5  // 收盤在所有均線之上
then ret = 1;
```

## 均線黃金交叉 + 量增

```xs
// 黃金交叉搭配量能確認
variable: ma5(0), ma20(0), avgVol(0);

ma5 = Average(Close, 5);
ma20 = Average(Close, 20);
avgVol = Average(Volume, 20);

if ma5 Cross Over ma20              // 黃金交叉
   AND Volume > avgVol * 1.5         // 量增50%
   AND Close > ma20                  // 收盤站上均線
then ret = 1;
```

## RSI 超賣反轉

```xs
// RSI由超賣區回升
variable: rsiVal(0);

rsiVal = RSI(Close, 14);

// RSI從30以下回升到30以上
if rsiVal Cross Over 30
   AND Close > Close[1]   // 今日收紅
then ret = 1;
```

## 突破近期新高

```xs
// 創20日新高 + 量增
variable: high20(0), avgVol(0);

high20 = Highest(High, 20)[1];  // 前20日最高（不含今日）
avgVol = Average(Volume, 20);

if Close > high20                    // 突破前高
   AND Volume > avgVol * 2           // 量增100%
   AND Close > Open                  // 收紅K
then ret = 1;
```

## 布林通道收斂突破

```xs
// 帶寬收斂後向上突破
variable: midBand(0), upperBand(0), lowerBand(0);
variable: bandWidth(0), avgBW(0);

midBand = Average(Close, 20);
upperBand = midBand + 2 * StandardDev(Close, 20);
lowerBand = midBand - 2 * StandardDev(Close, 20);

if midBand <> 0 then
  bandWidth = (upperBand - lowerBand) / midBand * 100;

avgBW = Average(bandWidth, 60);

// 帶寬小於歷史均值 + 突破上軌
if bandWidth < avgBW * 0.6   // 帶寬收斂
   AND Close > upperBand     // 突破上軌
   AND Volume > Average(Volume, 20)  // 有量
then ret = 1;
```

## KD 低檔黃金交叉

```xs
// KD指標低檔交叉
variable: kVal(0), dVal(0), rsv(0);

rsv = (Close - Lowest(Low, 9)) / (Highest(High, 9) - Lowest(Low, 9)) * 100;
kVal = XAverage(rsv, 3);
dVal = XAverage(kVal, 3);

if kVal Cross Over dVal     // K穿越D
   AND kVal < 30            // 在低檔區
   AND Close > Average(Close, 20)  // 站上均線
then ret = 1;
```

## 量縮整理後量增突破

```xs
// 先量縮整理，再量增突破
variable: avgVol5(0), avgVol20(0), ma20(0);

avgVol5 = Average(Volume, 5);
avgVol20 = Average(Volume, 20);
ma20 = Average(Close, 20);

// 前5日量縮(近5日均量<20日均量一半)
// 今日量增突破
if avgVol5[1] < avgVol20 * 0.5   // 前期量縮
   AND Volume > avgVol20 * 2      // 今日爆量
   AND Close > ma20               // 站上均線
   AND Close > Open               // 收紅
then ret = 1;
```
