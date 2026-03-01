# 指標範例：布林通道 + ATR

## 布林通道 (Bollinger Bands)

```xs
// 標準布林通道
input: _period(20, "均線週期");
input: _numStdDev(2, "標準差倍數");

variable: _midBand(0), _upperBand(0), _lowerBand(0);
variable: _bandWidth(0), _percentB(0);

_midBand = Average(Close, _period);
_upperBand = _midBand + _numStdDev * StandardDev(Close, _period);
_lowerBand = _midBand - _numStdDev * StandardDev(Close, _period);

Plot1(_upperBand, "上軌");
Plot2(_midBand, "中軌");
Plot3(_lowerBand, "下軌");
```

## 布林帶寬與 %B

```xs
// 帶寬收斂 = 即將突破的信號
input: _period(20, "週期");
input: _numStdDev(2, "標準差");

variable: _midBand(0), _upperBand(0), _lowerBand(0);
variable: _bandWidth(0), _percentB(0);

_midBand = Average(Close, _period);
_upperBand = _midBand + _numStdDev * StandardDev(Close, _period);
_lowerBand = _midBand - _numStdDev * StandardDev(Close, _period);

// 帶寬 = (上軌-下軌)/中軌
if _midBand <> 0 then
  _bandWidth = (_upperBand - _lowerBand) / _midBand * 100;

// %B = (收盤-下軌)/(上軌-下軌)
if (_upperBand - _lowerBand) <> 0 then
  _percentB = (Close - _lowerBand) / (_upperBand - _lowerBand) * 100;

Plot1(_bandWidth, "帶寬%");
Plot2(_percentB, "%B");
Plot3(80, "超買");
Plot4(20, "超賣");
```

## ATR (Average True Range)

```xs
// 平均真實波幅
input: _atrPeriod(14, "ATR週期");

variable: _trueRange(0), _atrValue(0);

// 真實波幅 = Max(當日高低差, 前收到今高, 前收到今低)
_trueRange = TrueRange;

// ATR = 真實波幅的移動平均
_atrValue = AvgTrueRange(_atrPeriod);

Plot1(_atrValue, "ATR");
```

## ATR 通道

```xs
// 基於ATR的動態通道
input: _atrPeriod(14, "ATR週期");
input: _atrMult(2, "ATR倍數");
input: _maPeriod(20, "均線週期");

variable: _atrVal(0), _maVal(0);
variable: _upperCh(0), _lowerCh(0);

_atrVal = AvgTrueRange(_atrPeriod);
_maVal = Average(Close, _maPeriod);

_upperCh = _maVal + _atrMult * _atrVal;
_lowerCh = _maVal - _atrMult * _atrVal;

Plot1(_upperCh, "ATR上軌");
Plot2(_maVal, "均線");
Plot3(_lowerCh, "ATR下軌");
```

## ATR 波動率指標

```xs
// 波動率相對高低判斷
input: _atrPeriod(14, "ATR週期");
input: _lookback(100, "回顧期間");

variable: _atrVal(0), _atrHigh(0), _atrLow(0), _atrPct(0);

_atrVal = AvgTrueRange(_atrPeriod);
_atrHigh = Highest(_atrVal, _lookback);
_atrLow = Lowest(_atrVal, _lookback);

// ATR百分位：0=極低波動, 100=極高波動
if (_atrHigh - _atrLow) <> 0 then
  _atrPct = (_atrVal - _atrLow) / (_atrHigh - _atrLow) * 100;

Plot1(_atrPct, "ATR百分位");
Plot2(80, "高波動");
Plot3(20, "低波動");
```
