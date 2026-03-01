# 警示範例：即時報價警示 (GetQuote)

> 使用 `GetQuote("欄位名")` 取得即時報價數據的警示腳本

## 即時價格突破均線

```xs
// 即時價格突破20日均線
variable: _price(0), _ma20(0);

_price = GetQuote("成交");
_ma20 = Average(Close, 20);

if _price > _ma20 AND Close[1] < _ma20 then
  ret = 1;
```

## 即時漲幅警示

```xs
// 漲幅超過5%
variable: _chgPct(0);

_chgPct = GetQuote("漲跌幅");

if _chgPct > 5 then
  ret = 1;
```

## 即時量能爆發

```xs
// 盤中量已超過昨量
variable: _todayVol(0), _yVol(0);

_todayVol = GetQuote("總量(日)");
_yVol = GetQuote("昨量");

if _todayVol > _yVol then
  ret = 1;
```

## 估計量突增

```xs
// 預估量超過昨量2倍（台股/大盤）
variable: _estVol(0), _yVol(0);

_estVol = GetQuote("估計量");
_yVol = GetQuote("昨量");

if _estVol > _yVol * 2 then
  ret = 1;
```

## 觸及漲停價

```xs
// 即時價格觸及漲停（台股/期貨）
variable: _price(0), _upLimit(0);

_price = GetQuote("成交");
_upLimit = GetQuote("漲停價");

if _price >= _upLimit AND _upLimit > 0 then
  ret = 1;
```

## 五檔委買賣失衡

```xs
// 委買遠大於委賣 = 買盤強勁
variable: _totalBid(0), _totalAsk(0);

_totalBid = GetQuote("總委買");
_totalAsk = GetQuote("總委賣");

// 委買是委賣的2倍以上
if _totalAsk > 0 AND _totalBid / _totalAsk > 2 then
  ret = 1;
```

## 外盤量佔比警示

```xs
// 外盤量佔比高 = 主動買盤強
variable: _outerVol(0), _innerVol(0), _totalVol(0);

_outerVol = GetQuote("外盤量");
_innerVol = GetQuote("內盤量");
_totalVol = _outerVol + _innerVol;

// 外盤佔比超過65%
if _totalVol > 0 AND _outerVol / _totalVol > 0.65 then
  ret = 1;
```

## 盤中價格接近支撐

```xs
// 即時價格接近前日低點（支撐位）
variable: _price(0), _yClose(0);

_price = GetQuote("成交");
_yClose = GetQuote("參考價");

// 價格在昨收-2%以內（接近支撐）
if _price < _yClose * 0.98
   AND _price > _yClose * 0.95  // 還未跌破太多
then ret = 1;
```

## 即時振幅警示

```xs
// 盤中振幅過大
variable: _amp(0);

_amp = GetQuote("振幅");

// 振幅超過7%
if _amp > 7 then
  ret = 1;
```

## 即時 Greeks 警示（選擇權）

```xs
// 選擇權Delta接近0.5 = 價平附近
variable: _delta(0), _iv(0);

_delta = GetQuote("Delta");
_iv = GetQuote("隱含波動率");

// Delta在0.4~0.6且IV偏低
if Abs(_delta) > 0.4 AND Abs(_delta) < 0.6
   AND _iv < 20
then ret = 1;
```
