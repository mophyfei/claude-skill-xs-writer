# Quote 市場統計欄位 (4) - 僅大盤/類股指數

> 用於 `GetQuote("欄位名")` 即時報價，僅適用大盤指數與類股指數

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 漲停家數 | UpLimitSecs | 大盤/類股指數 | 漲停股票家數 |
| 跌停家數 | DownLimitSecs | 大盤/類股指數 | 跌停股票家數 |
| 上漲家數 | UpSecs | 大盤/類股指數 | 上漲股票家數 |
| 下跌家數 | DownSecs | 大盤/類股指數 | 下跌股票家數 |

## 使用範例

```xs
// 判斷市場多空氣氛
upCount = GetQuote("UpSecs");
downCount = GetQuote("DownSecs");
if upCount > downCount * 2 then
  ret = 1;  // 強勢市場
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
