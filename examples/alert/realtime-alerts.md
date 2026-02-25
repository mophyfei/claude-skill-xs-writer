# 警示範例：即時報價警示 (GetQuote)

> 使用 `GetQuote("欄位名")` 取得即時報價數據的警示腳本

## 即時價格突破均線

```xs
// 即時價格突破20日均線
variable: price(0), ma20(0);

price = GetQuote("成交");
ma20 = Average(Close, 20);

if price > ma20 AND Close[1] < ma20 then
  ret = 1;
```

## 即時漲幅警示

```xs
// 漲幅超過5%
variable: chgPct(0);

chgPct = GetQuote("漲幅(%)");

if chgPct > 5 then
  ret = 1;
```

## 即時量能爆發

```xs
// 盤中量已超過昨量
variable: todayVol(0), yVol(0);

todayVol = GetQuote("總量(日)");
yVol = GetQuote("昨量");

if todayVol > yVol then
  ret = 1;
```

## 估計量突增

```xs
// 預估量超過昨量2倍（台股/大盤）
variable: estVol(0), yVol(0);

estVol = GetQuote("估計量");
yVol = GetQuote("昨量");

if estVol > yVol * 2 then
  ret = 1;
```

## 觸及漲停價

```xs
// 即時價格觸及漲停（台股/期貨）
variable: price(0), upLimit(0);

price = GetQuote("成交");
upLimit = GetQuote("漲停價");

if price >= upLimit AND upLimit > 0 then
  ret = 1;
```

## 五檔委買賣失衡

```xs
// 委買遠大於委賣 = 買盤強勁
variable: totalBid(0), totalAsk(0);

totalBid = GetQuote("總委買");
totalAsk = GetQuote("總委賣");

// 委買是委賣的2倍以上
if totalAsk > 0 AND totalBid / totalAsk > 2 then
  ret = 1;
```

## 外盤量佔比警示

```xs
// 外盤量佔比高 = 主動買盤強
variable: outerVol(0), innerVol(0), totalVol(0);

outerVol = GetQuote("外盤量");
innerVol = GetQuote("內盤量");
totalVol = outerVol + innerVol;

// 外盤佔比超過65%
if totalVol > 0 AND outerVol / totalVol > 0.65 then
  ret = 1;
```

## 盤中價格接近支撐

```xs
// 即時價格接近前日低點（支撐位）
variable: price(0), yClose(0), yLow(0);

price = GetQuote("成交");
yClose = GetQuote("昨收");

// 價格在昨收-2%以內（接近支撐）
if price < yClose * 0.98
   AND price > yClose * 0.95  // 還未跌破太多
then ret = 1;
```

## 即時振幅警示

```xs
// 盤中振幅過大
variable: amp(0);

amp = GetQuote("振幅(%)");

// 振幅超過7%
if amp > 7 then
  ret = 1;
```

## 即時 Greeks 警示（選擇權）

```xs
// 選擇權Delta接近0.5 = 價平附近
variable: delta(0), iv(0);

delta = GetQuote("Delta");
iv = GetQuote("隱含波動率");

// Delta在0.4~0.6且IV偏低
if Abs(delta) > 0.4 AND Abs(delta) < 0.6
   AND iv < 20
then ret = 1;
```
