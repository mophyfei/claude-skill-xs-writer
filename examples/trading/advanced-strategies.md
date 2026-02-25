# 交易範例：進階策略

## RSI 超買超賣策略

```xs
// RSI策略：超賣買進、超買賣出
input: rsiPeriod(14, "RSI週期");
input: oversold(30, "超賣門檻");
input: overbought(70, "超買門檻");

variable: rsiVal(0);

rsiVal = RSI(Close, rsiPeriod);

// RSI由超賣區回升
if rsiVal Cross Over oversold then
  SetPosition(1);

// RSI進入超買區
if rsiVal Cross Under overbought then
  SetPosition(0);
```

## 均線交叉策略（含口數轉換）

```xs
// 均線策略 + 台股口數轉換
// 台股交易單位：張 (1張=1000股)
// 期貨交易單位：口
input: capital(1000000, "投入資金");
input: riskPct(2, "風險百分比");

variable: maShort(0), maLong(0);
variable: atrVal(0), lots(0), riskAmount(0);

maShort = Average(Close, 10);
maLong = Average(Close, 30);
atrVal = AvgTrueRange(14);

// 計算口數：風險金額 / (ATR * 每點價值)
// 台股：每張=1000股，風險=ATR*1000
riskAmount = capital * riskPct / 100;
if atrVal * 1000 > 0 then
  lots = IntPortion(riskAmount / (atrVal * 1000));

if lots < 1 then lots = 1;

// 進出場
if maShort Cross Over maLong then
  SetPosition(1, lots);

if maShort Cross Under maLong then
  SetPosition(0);
```

## 突破策略 + 假突破過濾

```xs
// Donchian通道突破 + 量能確認
input: breakPeriod(20, "突破週期");
input: volMult(1.5, "量能倍數");

variable: upperBreak(0), lowerBreak(0);
variable: avgVol(0), volConfirm(false);

upperBreak = Highest(High, breakPeriod)[1];
lowerBreak = Lowest(Low, breakPeriod)[1];
avgVol = Average(Volume, 20);

// 量能確認：成交量需大於均量的倍數
volConfirm = Volume > avgVol * volMult;

// 向上突破 + 量能確認
if Close > upperBreak AND volConfirm then
  SetPosition(1);

// 向下突破
if Close < lowerBreak then
  SetPosition(0);
```

## 多指標綜合策略

```xs
// 結合均線+RSI+MACD的綜合策略
variable: ma20(0), ma60(0);
variable: rsiVal(0);
variable: macdLine(0), signalLine(0);
variable: bullCount(0);

ma20 = Average(Close, 20);
ma60 = Average(Close, 60);
rsiVal = RSI(Close, 14);
macdLine = XAverage(Close, 12) - XAverage(Close, 26);
signalLine = XAverage(macdLine, 9);

// 計算多頭信號數量
bullCount = 0;
if Close > ma20 then bullCount = bullCount + 1;
if ma20 > ma60 then bullCount = bullCount + 1;
if rsiVal > 50 AND rsiVal < 80 then bullCount = bullCount + 1;
if macdLine > signalLine then bullCount = bullCount + 1;

// 3個以上多頭信號才進場
if GetMarketPosition = 0 AND bullCount >= 3 then
  SetPosition(1);

// 信號不足2個時出場
if GetMarketPosition = 1 AND bullCount < 2 then
  SetPosition(0);
```

## 期貨日內當沖策略

```xs
// 期貨當沖：開盤突破策略
variable: openRangeHigh(0), openRangeLow(0);
variable: rangeSet(false);

// 前30分鐘建立開盤區間
if Time = 090000 then begin
  openRangeHigh = High;
  openRangeLow = Low;
  rangeSet = false;
end;

if Time > 090000 AND Time <= 093000 then begin
  if High > openRangeHigh then openRangeHigh = High;
  if Low < openRangeLow then openRangeLow = Low;
end;

if Time = 093000 then rangeSet = true;

// 突破開盤區間交易
if rangeSet AND Time > 093000 AND Time < 133000 then begin
  if Close > openRangeHigh then
    SetPosition(1);
  if Close < openRangeLow then
    SetPosition(-1);
end;

// 收盤前平倉
if Time >= 133000 then
  SetPosition(0);
```
