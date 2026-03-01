# 交易範例：進階策略

## RSI 超買超賣策略

```xs
// RSI策略：超賣買進、超買賣出
input: _rsiPeriod(14, "RSI週期");
input: _oversold(30, "超賣門檻");
input: _overbought(70, "超買門檻");

variable: _rsiVal(0);

_rsiVal = RSI(Close, _rsiPeriod);

// RSI由超賣區回升
if _rsiVal Cross Over _oversold then
  SetPosition(1);

// RSI進入超買區
if _rsiVal Cross Under _overbought then
  SetPosition(0);
```

## 均線交叉策略（含口數轉換）

```xs
// 均線策略 + 台股口數轉換
// 台股交易單位：張 (1張=1000股)
// 期貨交易單位：口
input: _capital(1000000, "投入資金");
input: _riskPct(2, "風險百分比");

variable: _maShort(0), _maLong(0);
variable: _atrVal(0), _lots(0), _riskAmount(0);

_maShort = Average(Close, 10);
_maLong = Average(Close, 30);
_atrVal = AvgTrueRange(14);

// 計算口數：風險金額 / (ATR * 每點價值)
// 台股：每張=1000股，風險=ATR*1000
_riskAmount = _capital * _riskPct / 100;
if _atrVal * 1000 > 0 then
  _lots = IntPortion(_riskAmount / (_atrVal * 1000));

if _lots < 1 then _lots = 1;

// 進出場
if _maShort Cross Over _maLong then
  SetPosition(1, _lots);

if _maShort Cross Under _maLong then
  SetPosition(0);
```

## 突破策略 + 假突破過濾

```xs
// Donchian通道突破 + 量能確認
input: _breakPeriod(20, "突破週期");
input: _volMult(1.5, "量能倍數");

variable: _upperBreak(0), _lowerBreak(0);
variable: _avgVol(0), _volConfirm(false);

_upperBreak = Highest(High, _breakPeriod)[1];
_lowerBreak = Lowest(Low, _breakPeriod)[1];
_avgVol = Average(Volume, 20);

// 量能確認：成交量需大於均量的倍數
_volConfirm = Volume > _avgVol * _volMult;

// 向上突破 + 量能確認
if Close > _upperBreak AND _volConfirm then
  SetPosition(1);

// 向下突破
if Close < _lowerBreak then
  SetPosition(0);
```

## 多指標綜合策略

```xs
// 結合均線+RSI+MACD的綜合策略
variable: _ma20(0), _ma60(0);
variable: _rsiVal(0);
variable: _macdLine(0), _signalLine(0);
variable: _bullCount(0);

_ma20 = Average(Close, 20);
_ma60 = Average(Close, 60);
_rsiVal = RSI(Close, 14);
_macdLine = XAverage(Close, 12) - XAverage(Close, 26);
_signalLine = XAverage(_macdLine, 9);

// 計算多頭信號數量
_bullCount = 0;
if Close > _ma20 then _bullCount = _bullCount + 1;
if _ma20 > _ma60 then _bullCount = _bullCount + 1;
if _rsiVal > 50 AND _rsiVal < 80 then _bullCount = _bullCount + 1;
if _macdLine > _signalLine then _bullCount = _bullCount + 1;

// 3個以上多頭信號才進場
if GetMarketPosition = 0 AND _bullCount >= 3 then
  SetPosition(1);

// 信號不足2個時出場
if GetMarketPosition = 1 AND _bullCount < 2 then
  SetPosition(0);
```

## 期貨日內當沖策略

```xs
// 期貨當沖：開盤突破策略
variable: _openRangeHigh(0), _openRangeLow(0);
variable: _rangeSet(false);

// 前30分鐘建立開盤區間
if Time = 090000 then begin
  _openRangeHigh = High;
  _openRangeLow = Low;
  _rangeSet = false;
end;

if Time > 090000 AND Time <= 093000 then begin
  if High > _openRangeHigh then _openRangeHigh = High;
  if Low < _openRangeLow then _openRangeLow = Low;
end;

if Time = 093000 then _rangeSet = true;

// 突破開盤區間交易
if _rangeSet AND Time > 093000 AND Time < 133000 then begin
  if Close > _openRangeHigh then
    SetPosition(1);
  if Close < _openRangeLow then
    SetPosition(-1);
end;

// 收盤前平倉
if Time >= 133000 then
  SetPosition(0);
```
