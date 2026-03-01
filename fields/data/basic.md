# Data 基本欄位 (9)

> 用於 `GetField("欄位名")` 歷史資料

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 投資建議評級 | RecommendationRating | 美(股票) | | 市場機構對個股的投資建議評等分數。 |
| 月營收 | Sales | 台股 大盤 | | 每個月的營業收入。 |
| 本益比 | PE | 台(股票) 美(股票) | | 股票的本益比。 |
| 殖利率 | Yield | 台(股票) 美(股票) 美(特別股) 美(ETF) | | 股票的殖利率。單位是%，例如殖利率為5.6％的話，則回傳5.6。 |
| 發行張數(張) | OutStandingShares | 台股 | | 當期的發行張數。 |
| 總市值(元) | TotalMarketValue | 台股 大盤 類股指數 | | 股票或是指數的市值。股票市值以發行股數 ＊ 收盤價來計算，指數則是成分股的市值加 |
| 股本(億) | CurrentCapitalinBillion | 台股 | | 股票的股本，換算成億元。 |
| 股本(元) | CurrentCapital | 台股 | | 股票的股本，換算成元。 |
| 財報股本(億) | CurrentCapitalin100Million | 台股 | | 公司財報(季、年)上載明的股本，換算成億元。 |

## 使用範例

```xs
cap = GetField("總市值(元)");  // 或 GetField("TotalMarketValue")
pe = GetField("本益比");  // 或 GetField("PE")
```

> 欄位名稱以 xs-helper 官方文件為準
