# Quote 常用欄位 (12)

> 用於 `GetQuote("欄位名")` 即時報價

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 估計量 | EstimatedTotalVolume | 大盤 台(股票) | | 當日收盤的預估成交量。也可以使用 GetField("估計量", "D") 來表 |
| 參考價 | RefPrice | 台股 | | 當日的參考價。也可以使用 GetField("RefPrice", "D") 來 |
| 單量 | TickVolume | 全部 | | 最後一筆成交的單量。也可以使用 GetField("Volume", "Tick |
| 成交 | Last | 全部 | | 最新一筆成交的價格。等同於 Close 。 |
| 成交時間 | Time | 全部 | | 最新一筆成交的時間。也可以使用 GetField("Time", "Tick") |
| 昨量 | PreTotalVolume | 全部 | | 前一個交易日的盤中成交量，不包含零股以及鉅額交易。 |
| 最低(日) | DailyLow | 全部 | | 當日的最低價。也可以使用 GetField("Low", "D") 來表示。 |
| 最高(日) | DailyHigh | 全部 | | 當日的最高價。也可以使用 GetField("High", "D") 來表示。 |
| 總量(日) | DailyVolume | 全部 | | 當日的總成交量。也可以使用 GetField("Volume", "D") 來表 |
| 買進 | Bid | 台股 期貨 選擇權 香港股票 大陸股票 美(股票) | | 目前委託簿內買方最高的買價。 |
| 賣出 | Ask | 台股 期貨 選擇權 香港股票 大陸股票 美(股票) | | 目前委託簿內賣方最低的賣價。 |
| 開盤(日) | DailyOpen | 全部 | | 當日的開盤價。也可以使用 GetField("Open", "D") 來表示。 |

## 使用範例

```xs
value1 = GetQuote("成交");  // 或 GetQuote("Last")
value2 = GetQuote("總量(日)");  // 或 GetQuote("DailyVolume")
```

> 欄位名稱以 xs-helper 官方文件為準
