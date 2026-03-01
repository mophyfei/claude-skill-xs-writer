# Quote 量能欄位 (27)

> 用於 `GetQuote("欄位名")` 即時報價

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 估計量 | EstimatedTotalVolume | 大盤 台(股票) | | 當日收盤的預估成交量。也可以使用 GetField("估計量", "D") 來表 |
| 內盤量 | InSize | 台股 大盤 類股指數 期貨 選擇權 香港股票 大陸股票 | | 當日累計迄今的內盤量。也可以使用 GetField("內盤量", "D") 來表 |
| 單量 | TickVolume | 全部 | | 最後一筆成交的單量。也可以使用 GetField("Volume", "Tick |
| 外盤量 | OutSize | 台股 大盤 類股指數 期貨 選擇權 香港股票 大陸股票 | | 當日累計迄今的外盤量。也可以使用 GetField("外盤量", "D") 來表 |
| 委買均 | AvgLongUnits | 大盤 期貨 選擇權 | | 每一筆委買的平均張數/口數。 |
| 委賣均 | AvgShortUnits | 大盤 期貨 選擇權 | | 每一筆委賣的平均張數/口數。 |
| 成交均量 | AvgDealedShare | 大盤 | | 整體市場(扣除權證)的每筆成交平均張數。 |
| 成交比重 | CashDirect | 台股 類股指數 | | 成交值占對應大盤的成交比重(％)。 |
| 成交金額(元) | TotalAmount | 台股 大盤 類股指數 香港股票 大陸股票 美(股票) | | 當日的總成交金額。也可以使用 GetField("成交金額", "D") 來表示 |
| 昨量 | PreTotalVolume | 全部 | | 前一個交易日的盤中成交量，不包含零股以及鉅額交易。 |
| 累委買筆 | CulBidTicks | 大盤 期貨 選擇權 | | 開盤迄今的總委買筆數。也可以使用 GetField("累委買筆", "D") 來 |
| 累委賣筆 | CulAskTicks | 大盤 期貨 選擇權 | | 開盤迄今的總委賣筆數。也可以使用 GetField("累委賣筆", "D") 來 |
| 累成交筆 | CulMatchTicks | 大盤 | | 開盤迄今整體市場(扣除權證)的成交總筆數。也可以使用 GetField("累成交 |
| 累計委買 | BidUnits | 大盤 期貨 選擇權 | | 開盤迄今的總委買張數/口數。也可以使用 GetField("累計委買", "D" |
| 累計委賣 | AskUnits | 大盤 期貨 選擇權 | | 開盤迄今的總委賣張數/口數。也可以使用 GetField("累計委賣", "D" |
| 累計成交 | MatchUnit | 大盤 期貨 選擇權 | | 開盤迄今的總成交張數/口數，也可以使用GetField("累計成交", "D") |
| 累買成筆 | CulBuyTicks | 期貨 選擇權 | | 開盤迄今以買進成交的總筆數。也可以使用GetField("累買成筆", "D") |
| 累賣成筆 | CulSellTicks | 期貨 選擇權 | | 開盤迄今以賣出成交的總筆數。也可以使用GetField("累賣成筆", "D") |
| 總成交次數 | TotalTicks | 台股 期貨 選擇權 香港股票 大陸股票 美(股票) | | 當日到目前為止的成交明細資料總筆數。也可以使用 GetField("總成交次數" |
| 總量(日) | DailyVolume | 全部 | | 當日的總成交量。也可以使用 GetField("Volume", "D") 來表 |
| 量比 | VolumeRatio | 台(股票) 香港股票 大陸股票 | | 當日估計量對比昨日成交量的放大比例。 |
| 開盤委買 | BoughtLotsAtOpen | 台股 大盤 類股指數 期貨 選擇權 | | 開盤時委託買進的數量。也可以使用 GetField("開盤委買", "D") 來 |
| 開盤委賣 | SoldLotsAtOpen | 台股 大盤 類股指數 期貨 選擇權 | | 開盤時委託賣出的數量。也可以使用 GetField("開盤委賣", "D") 來 |
| 開盤買均 | BoughtAverageAtOpen | 大盤 期貨 選擇權 | | 開盤時每筆委託買進張數/口數。 |
| 開盤買筆 | BoughtTickAtOpen | 大盤 期貨 選擇權 | | 開盤時委託買進的筆數。也可以使用GetField("開盤買筆", "D")來表示 |
| 開盤賣均 | SoldAverageAtOpen | 大盤 期貨 選擇權 | | 開盤時每筆委託賣出張數/口數。 |
| 開盤賣筆 | SoldTickAtOpen | 大盤 期貨 選擇權 | | 開盤時委託賣出的筆數。也可以使用GetField("開盤賣筆", "D")來表示 |

## 使用範例

```xs
vol = GetQuote("總量(日)");  // 或 GetQuote("DailyVolume")
yestVol = GetQuote("昨量");  // 或 GetQuote("PreTotalVolume")
ratio = vol / yestVol;
```

> 欄位名稱以 xs-helper 官方文件為準
