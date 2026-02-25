# 交易範例：進出場基本模式

## 基本買賣 - SetPosition

```xs
// SetPosition 基本用法
// SetPosition(1)  = 做多 (買進)
// SetPosition(-1) = 做空 (賣出)
// SetPosition(0)  = 平倉 (出場)

// 均線黃金交叉買進，死亡交叉賣出
variable: maShort(0), maLong(0);

maShort = Average(Close, 5);
maLong = Average(Close, 20);

if maShort Cross Over maLong then
  SetPosition(1)    // 買進
else if maShort Cross Under maLong then
  SetPosition(0);   // 平倉
```

## 指定口數買賣

```xs
// SetPosition 搭配口數
// SetPosition(1, 2) = 做多2口/張

variable: rsiVal(0);

rsiVal = RSI(Close, 14);

if rsiVal < 30 then
  SetPosition(1, 2)     // RSI超賣，買2口
else if rsiVal < 20 then
  SetPosition(1, 4)     // RSI極度超賣，買4口
else if rsiVal > 70 then
  SetPosition(0);       // RSI超買，平倉
```

## Buy / Sell 語法

```xs
// Buy / Sell 語法（等同 SetPosition 簡寫）
// Buy = 做多進場
// Sell = 做多出場
// SellShort = 做空進場
// BuyToCover = 做空出場

variable: ma20(0);

ma20 = Average(Close, 20);

// 收盤站上20日均線買進
if Close > ma20 AND Close[1] <= ma20[1] then
  Buy("均線突破");

// 收盤跌破20日均線賣出
if Close < ma20 AND Close[1] >= ma20[1] then
  Sell("均線跌破");
```

## 多空雙向交易

```xs
// 同時處理多單與空單
variable: maShort(0), maLong(0);

maShort = Average(Close, 10);
maLong = Average(Close, 30);

// 多單進場
if maShort Cross Over maLong then begin
  SetPosition(1);
end;

// 空單進場
if maShort Cross Under maLong then begin
  SetPosition(-1);
end;
```

## 限定交易時間

```xs
// 僅在特定時間區間交易（適用期貨日內交易）
variable: maShort(0), maLong(0);
variable: canTrade(false);

maShort = Average(Close, 5);
maLong = Average(Close, 20);

// 限制交易時間：09:00 ~ 13:00
canTrade = Time >= 090000 AND Time <= 130000;

if canTrade then begin
  if maShort Cross Over maLong then
    SetPosition(1);
  if maShort Cross Under maLong then
    SetPosition(-1);
end;

// 收盤前平倉
if Time >= 133000 then
  SetPosition(0);
```

## 條件單進場

```xs
// 突破前高買進
variable: prevHigh(0);

prevHigh = Highest(High, 20)[1];  // 前20日最高（不含今日）

// 突破前高且量增
if Close > prevHigh
   AND Volume > Average(Volume, 20) * 1.5 then
  SetPosition(1);

// 跌破前低出場
if Close < Lowest(Low, 10)[1] then
  SetPosition(0);
```
