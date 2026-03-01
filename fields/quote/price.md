# Quote 價格欄位 (23)

> 用於 `GetQuote("欄位名")` 即時報價

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 一年前收盤價 | Close1Yago | 全部 | | 一年前的收盤價。可以用來計算區間漲跌幅。 |
| 一月前收盤價 | Close1Mago | 全部 | | 一個月前的收盤價。可以用來計算區間漲跌幅。 |
| 一週前收盤價 | Close1Wago | 全部 | | 五個交易日前的收盤價。可以用來計算區間漲跌幅。 |
| 三月前收盤價 | Close3Mago | 全部 | | 三個月前的收盤價。可以用來計算區間漲跌幅。 |
| 價差 | Spread | 大盤 期貨 | | 期貨價格與現貨價格之間的差額。 |
| 內外盤 | BidAskFlag | 全部 | | 最後一筆成交價的內外盤標記。數值是1時表示是外盤成交，數值是-1時為內盤成交，如 |
| 前一價 | PreMatch1 | 全部 | | 最新一筆成交價的前一筆成交價格。也可以使用 GetField("Close",  |
| 前三價 | PreMatch3 | 全部 | | 最新一筆成交價的前第三筆成交價格。也可以使用 GetField("Close", |
| 前二價 | PreMatch2 | 全部 | | 最新一筆成交價的前第二筆成交價格。也可以使用 GetField("Close", |
| 前四價 | PreMatch4 | 全部 | | 最新一筆成交價的前第四筆成交價格。也可以使用 GetField("Close", |
| 去年收盤價 | CloseOfLastYear | 全部 | | 去年最後一個交易日的收盤價。可以用來計算區間漲跌幅。 |
| 參考價 | RefPrice | 台股 | | 當日的參考價。也可以使用 GetField("RefPrice", "D") 來 |
| 均價 | AvgPrice | 台股 大盤 類股指數 台(權證) 期貨 選擇權 香港股票 大陸股票 美股 | | 當日的平均成交價。也可以使用 GetField("均價", "D") 來表示。 |
| 基差 | Basis | 大盤 期貨 | | 現貨價格與期貨價格之間的差異。也可以使用 GetField("基差") 來表示。 |
| 成交 | Last | 全部 | | 最新一筆成交的價格。等同於 Close 。 |
| 振幅 | DayAmplitude | 全部 | | 當日的振幅。 |
| 最低(日) | DailyLow | 全部 | | 當日的最低價。也可以使用 GetField("Low", "D") 來表示。 |
| 最高(日) | DailyHigh | 全部 | | 當日的最高價。也可以使用 GetField("High", "D") 來表示。 |
| 漲停價 | DailyUplimit | 台股 期貨 選擇權 大陸股票 | | 當日的漲停價。也可以使用 GetField("漲停價", "D") 來表示。 |
| 漲跌幅 | PriceChangeRatio | 全部 | | 當日的漲跌幅。 |
| 買賣價差百分比 | BidAskDiffRatio | 台股 期貨 選擇權 香港股票 大陸股票 美(股票) | | 買賣價差占買價的比例。 |
| 跌停價 | DailyDownlimit | 台股 期貨 選擇權 大陸股票 | | 當日的跌停價。也可以使用 GetField("跌停價", "D") 來表示。 |
| 開盤(日) | DailyOpen | 全部 | | 當日的開盤價。也可以使用 GetField("Open", "D") 來表示。 |

## 使用範例

```xs
high = GetQuote("最高(日)");  // 或 GetQuote("DailyHigh")
low = GetQuote("最低(日)");  // 或 GetQuote("DailyLow")
spread = high - low;
```

> 欄位名稱以 xs-helper 官方文件為準
