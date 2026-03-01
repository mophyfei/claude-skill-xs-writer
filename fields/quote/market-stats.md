# Quote 市場統計欄位 (4)

> 用於 `GetQuote("欄位名")` 即時報價
> 適用於大盤指數商品

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 上漲家數 | UpSecurities | 大盤 類股指數 | | 指數成分股內目前上漲的家數。也可以使用GetField("上漲家數", "D") |
| 下跌家數 | DownSecurities | 大盤 類股指數 | | 指數成分股內目前下跌的家數。也可以使用GetField("下跌家數", "D") |
| 漲停家數 | UpLimitSecs | 大盤 類股指數 | | 指數成分股內目前漲停的家數。也可以使用GetField("漲停家數", "D") |
| 跌停家數 | DownLimitSecs | 大盤 類股指數 | | 指數成分股內目前跌停的家數。也可以使用GetField("跌停家數", "D") |

## 使用範例

```xs
up = GetQuote("上漲家數");
down = GetQuote("下跌家數");
```

> 欄位名稱以 xs-helper 官方文件為準
