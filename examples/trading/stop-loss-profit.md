# 交易範例：停損停利

## 固定百分比停損

```xs
// 固定百分比停損
input: stopLossPct(5, "停損百分比");

variable: entryPrice(0), maShort(0), maLong(0);

maShort = Average(Close, 5);
maLong = Average(Close, 20);

// 進場
if maShort Cross Over maLong then begin
  SetPosition(1);
  entryPrice = Close;
end;

// 停損出場
if GetMarketPosition = 1 then begin
  if Close <= entryPrice * (1 - stopLossPct / 100) then
    SetPosition(0);  // 停損
end;
```

## 固定百分比停利

```xs
// 固定停損 + 固定停利
input: stopLossPct(5, "停損%");
input: takeProfitPct(10, "停利%");

variable: entryPrice(0);

// 進場條件
if GetMarketPosition = 0 AND Close > Average(Close, 20) then begin
  SetPosition(1);
  entryPrice = Close;
end;

// 停損停利
if GetMarketPosition = 1 then begin
  // 停損
  if Close <= entryPrice * (1 - stopLossPct / 100) then
    SetPosition(0);
  // 停利
  if Close >= entryPrice * (1 + takeProfitPct / 100) then
    SetPosition(0);
end;
```

## 移動停利 (Trailing Stop)

```xs
// 移動停利：跟隨最高點回撤一定比例出場
input: trailPct(5, "回撤百分比");

variable: entryPrice(0), highestSinceEntry(0);

// 進場
if GetMarketPosition = 0 AND Close Cross Over Average(Close, 60) then begin
  SetPosition(1);
  entryPrice = Close;
  highestSinceEntry = Close;
end;

// 持倉期間追蹤最高點
if GetMarketPosition = 1 then begin
  if Close > highestSinceEntry then
    highestSinceEntry = Close;

  // 從最高點回撤超過設定比例則出場
  if Close <= highestSinceEntry * (1 - trailPct / 100) then
    SetPosition(0);
end;
```

## ATR 動態停損

```xs
// 使用ATR計算動態停損距離
input: atrPeriod(14, "ATR週期");
input: atrMult(2, "ATR倍數");

variable: entryPrice(0), atrStop(0);
variable: atrVal(0);

atrVal = AvgTrueRange(atrPeriod);

// 進場
if GetMarketPosition = 0 AND Close Cross Over Average(Close, 20) then begin
  SetPosition(1);
  entryPrice = Close;
  atrStop = Close - atrMult * atrVal;
end;

// ATR停損：隨價格上漲調高停損點
if GetMarketPosition = 1 then begin
  value1 = Close - atrMult * atrVal;
  if value1 > atrStop then
    atrStop = value1;  // 只上調不下調

  if Close <= atrStop then
    SetPosition(0);
end;
```

## 分批停利

```xs
// 分批停利：達到目標分批出場
input: tp1Pct(5, "第一目標%");
input: tp2Pct(10, "第二目標%");

variable: entryPrice(0), lots(4), soldFirst(false);

// 進場4口
if GetMarketPosition = 0 AND Close Cross Over Average(Close, 20) then begin
  SetPosition(1, 4);
  entryPrice = Close;
  lots = 4;
  soldFirst = false;
end;

if GetMarketPosition = 1 then begin
  // 第一目標：賣2口
  if NOT soldFirst
     AND Close >= entryPrice * (1 + tp1Pct / 100) then begin
    SetPosition(1, 2);  // 減倉至2口
    soldFirst = true;
  end;

  // 第二目標：全部出場
  if Close >= entryPrice * (1 + tp2Pct / 100) then
    SetPosition(0);

  // 停損：全部出場
  if Close <= entryPrice * 0.95 then
    SetPosition(0);
end;
```
