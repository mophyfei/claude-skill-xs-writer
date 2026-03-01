# 交易範例：停損停利

## 固定百分比停損

```xs
// 固定百分比停損
input: _stopLossPct(5, "停損百分比");

variable: _entryPrice(0), _maShort(0), _maLong(0);

_maShort = Average(Close, 5);
_maLong = Average(Close, 20);

// 進場
if _maShort Cross Over _maLong then begin
  SetPosition(1);
  _entryPrice = Close;
end;

// 停損出場
if GetMarketPosition = 1 then begin
  if Close <= _entryPrice * (1 - _stopLossPct / 100) then
    SetPosition(0);  // 停損
end;
```

## 固定百分比停利

```xs
// 固定停損 + 固定停利
input: _stopLossPct(5, "停損%");
input: _takeProfitPct(10, "停利%");

variable: _entryPrice(0);

// 進場條件
if GetMarketPosition = 0 AND Close > Average(Close, 20) then begin
  SetPosition(1);
  _entryPrice = Close;
end;

// 停損停利
if GetMarketPosition = 1 then begin
  // 停損
  if Close <= _entryPrice * (1 - _stopLossPct / 100) then
    SetPosition(0);
  // 停利
  if Close >= _entryPrice * (1 + _takeProfitPct / 100) then
    SetPosition(0);
end;
```

## 移動停利 (Trailing Stop)

```xs
// 移動停利：跟隨最高點回撤一定比例出場
input: _trailPct(5, "回撤百分比");

variable: _entryPrice(0), _highestSinceEntry(0);

// 進場
if GetMarketPosition = 0 AND Close Cross Over Average(Close, 60) then begin
  SetPosition(1);
  _entryPrice = Close;
  _highestSinceEntry = Close;
end;

// 持倉期間追蹤最高點
if GetMarketPosition = 1 then begin
  if Close > _highestSinceEntry then
    _highestSinceEntry = Close;

  // 從最高點回撤超過設定比例則出場
  if Close <= _highestSinceEntry * (1 - _trailPct / 100) then
    SetPosition(0);
end;
```

## ATR 動態停損

```xs
// 使用ATR計算動態停損距離
input: _atrPeriod(14, "ATR週期");
input: _atrMult(2, "ATR倍數");

variable: _entryPrice(0), _atrStop(0);
variable: _atrVal(0);

_atrVal = AvgTrueRange(_atrPeriod);

// 進場
if GetMarketPosition = 0 AND Close Cross Over Average(Close, 20) then begin
  SetPosition(1);
  _entryPrice = Close;
  _atrStop = Close - _atrMult * _atrVal;
end;

// ATR停損：隨價格上漲調高停損點
if GetMarketPosition = 1 then begin
  value1 = Close - _atrMult * _atrVal;
  if value1 > _atrStop then
    _atrStop = value1;  // 只上調不下調

  if Close <= _atrStop then
    SetPosition(0);
end;
```

## 分批停利

```xs
// 分批停利：達到目標分批出場
input: _tp1Pct(5, "第一目標%");
input: _tp2Pct(10, "第二目標%");

variable: _entryPrice(0), _lots(4), _soldFirst(false);

// 進場4口
if GetMarketPosition = 0 AND Close Cross Over Average(Close, 20) then begin
  SetPosition(1, 4);
  _entryPrice = Close;
  _lots = 4;
  _soldFirst = false;
end;

if GetMarketPosition = 1 then begin
  // 第一目標：賣2口
  if NOT _soldFirst
     AND Close >= _entryPrice * (1 + _tp1Pct / 100) then begin
    SetPosition(1, 2);  // 減倉至2口
    _soldFirst = true;
  end;

  // 第二目標：全部出場
  if Close >= _entryPrice * (1 + _tp2Pct / 100) then
    SetPosition(0);

  // 停損：全部出場
  if Close <= _entryPrice * 0.95 then
    SetPosition(0);
end;
```
