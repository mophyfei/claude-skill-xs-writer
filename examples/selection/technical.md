# 選股範例：技術面

## 均線多頭排列

```xs
// 均線多頭排列選股
variable: _ma5(0), _ma10(0), _ma20(0), _ma60(0);

_ma5 = Average(Close, 5);
_ma10 = Average(Close, 10);
_ma20 = Average(Close, 20);
_ma60 = Average(Close, 60);

// 短>中>長 = 多頭排列
if _ma5 > _ma10 AND _ma10 > _ma20 AND _ma20 > _ma60
   AND Close > _ma5  // 收盤在所有均線之上
then ret = 1;
```

## 均線黃金交叉 + 量增

```xs
// 黃金交叉搭配量能確認
variable: _ma5(0), _ma20(0), _avgVol(0);

_ma5 = Average(Close, 5);
_ma20 = Average(Close, 20);
_avgVol = Average(Volume, 20);

if _ma5 Cross Over _ma20              // 黃金交叉
   AND Volume > _avgVol * 1.5         // 量增50%
   AND Close > _ma20                  // 收盤站上均線
then ret = 1;
```

## RSI 超賣反轉

```xs
// RSI由超賣區回升
variable: _rsiVal(0);

_rsiVal = RSI(Close, 14);

// RSI從30以下回升到30以上
if _rsiVal Cross Over 30
   AND Close > Close[1]   // 今日收紅
then ret = 1;
```

## 突破近期新高

```xs
// 創20日新高 + 量增
variable: _high20(0), _avgVol(0);

_high20 = Highest(High, 20)[1];  // 前20日最高（不含今日）
_avgVol = Average(Volume, 20);

if Close > _high20                    // 突破前高
   AND Volume > _avgVol * 2           // 量增100%
   AND Close > Open                  // 收紅K
then ret = 1;
```

## 布林通道收斂突破

```xs
// 帶寬收斂後向上突破
variable: _midBand(0), _upperBand(0), _lowerBand(0);
variable: _bandWidth(0), _avgBW(0);

_midBand = Average(Close, 20);
_upperBand = _midBand + 2 * StandardDev(Close, 20);
_lowerBand = _midBand - 2 * StandardDev(Close, 20);

if _midBand <> 0 then
  _bandWidth = (_upperBand - _lowerBand) / _midBand * 100;

_avgBW = Average(_bandWidth, 60);

// 帶寬小於歷史均值 + 突破上軌
if _bandWidth < _avgBW * 0.6   // 帶寬收斂
   AND Close > _upperBand     // 突破上軌
   AND Volume > Average(Volume, 20)  // 有量
then ret = 1;
```

## KD 低檔黃金交叉

```xs
// KD指標低檔交叉
variable: _kVal(0), _dVal(0), _rsv(0);

_rsv = (Close - Lowest(Low, 9)) / (Highest(High, 9) - Lowest(Low, 9)) * 100;
_kVal = XAverage(_rsv, 3);
_dVal = XAverage(_kVal, 3);

if _kVal Cross Over _dVal     // K穿越D
   AND _kVal < 30            // 在低檔區
   AND Close > Average(Close, 20)  // 站上均線
then ret = 1;
```

## 量縮整理後量增突破

```xs
// 先量縮整理，再量增突破
variable: _avgVol5(0), _avgVol20(0), _ma20(0);

_avgVol5 = Average(Volume, 5);
_avgVol20 = Average(Volume, 20);
_ma20 = Average(Close, 20);

// 前5日量縮(近5日均量<20日均量一半)
// 今日量增突破
if _avgVol5[1] < _avgVol20 * 0.5   // 前期量縮
   AND Volume > _avgVol20 * 2      // 今日爆量
   AND Close > _ma20               // 站上均線
   AND Close > Open               // 收紅
then ret = 1;
```
