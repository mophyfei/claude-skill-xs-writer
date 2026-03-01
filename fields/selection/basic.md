# Selection 基本欄位 (34)

> 用於選股腳本
> 公司基本資料、股利、市值等

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 公司成立日期 | FoundingDate | 台股 美(ETF) | | 公司成立日期。 |
| 公司掛牌日期 | ListingDate | 台股 | | 公司上櫃或是上市的日期。 |
| 公司類別 | CompanySize | 台股 | | 系統運用市值，將公司分為大型股、中型股、小型股。 |
| 公司風格 | CompanyStyle | 台股 | | 系統運用財務數值評價，將公司分為混合型、價值型、成長型。 |
| 公積配股 | DividendFromCapitalReserve | 台股 | | 股票股利內的公積配股。 |
| 員工人數 | Numemployees | 台股 美(股票) | | 來自年報的員工總人數。 |
| 員工配股率 | RatioOfEmployeeBonus－Stock | 台股 | | 計算公式 : 員工分紅股數 / 已發行股數\*100%。 |
| 填息天數 | DaysForCashDividendAdjustment | 台股 | | 填息天數，指的是在股票除息後，股價從除息參考價回升至除息前收盤價所需的天數。 |
| 填權天數 | DaysForStockDividendAdjustment | 台股 | | 填權天數，指的是在股票除權後，股價從除權參考價回升至除權前收盤價所需的天數。 |
| 投資建議評級 | RecommendationRating | 美(股票) | | 市場機構對個股的投資建議評等分數。 |
| 新產能預計量產日期 | DateOfNewProductionCapacity | 台股 | | 最近可能增加產能的預估量產日期。 |
| 月營收 | Sales | 台股 | | 台股上市櫃公司每月公告的營業收入數值。 |
| 月營收年增率 | Sales－YoY | 台股 | | 商品當月營收較去年同月營收的成長率。 |
| 月營收月增率 | Sales－MoM | 台股 | | 商品當月營收較上一月營收的成長率。 |
| 殖利率 | Yield | 台股 美(股票) 美(特別股) 美(ETF) | | 股票的殖利率。單位是%，例如殖利率為5.6％的話，則回傳5.6。 |
| 現金股利 | CashDividend | 台股 美(股票) 美(特別股) 美(ETF) | | 現金配發的股利(股息)。 |
| 現金股利佔股利比重 | CashDividend／TotalDividend | 台股 | | 計算公式：現金股利 / (現金股利+股票股利) \* 100%。 |
| 現金股利殖利率 | CashDividendYield | 台股 | | 現金股利相對於股價的比例，用來衡量股票投資的回報。 |
| 發行張數(張) | OutStandingShares | 台股 | | 當期的發行張數。 |
| 發行張數(萬張) | OutStandingShares | 台股 | | 當期的發行張數。單位是萬張。 |
| 盈餘配股 | DividendFromEarning | 台股 | | 股票股利內的盈餘配股項目。 |
| 累計營收 | AccSales | 台股 | | 年初迄今公告的月營收累計總金額。 |
| 累計營收年增率 | AccSales－YoY | 台股 | | 商品今年以來累計營收較去年同期累計營收的成長率。 |
| 總市值(億) | MarketCapin100Million | 台股 類股指數 | | 股票或是指數的市值，換算成億元。股票市值以發行股數 ＊ 收盤價來計算，指數則是成 |
| 總市值(元) | TotalMarketValue | 台股 類股指數 美(股票) | | 股票或是指數的市值。股票市值以發行股數 ＊ 收盤價來計算，指數則是成分股的市值加 |
| 總經理 | GeneralManager | 台股 | | 目前總經理的姓名。 |
| 股利合計 | TotalDividend | 台股 | | 最近一個完整股利年度的現金股利＋股票股利。 |
| 股本(億) | Capital-Lastest | 台股 | | 股票的股本，換算成億元。 |
| 股本(元) | CurrentCapital | 台股 | | 股票的股本，換算成元。 |
| 股票股利 | StockDividend | 台股 | | 最近一個完整股利年度的股票股利。 |
| 股票股利佔股利比重 | StockDividend／TotalDividend | 台股 | | 計算公式：股票股利 / (現金股利+股票股利) \*100%。 |
| 股票股利殖利率 | StockDividendYield | 台股 | | 股票股利(配股)相對於股價的比例。 |
| 董事長 | Chairman | 台股 | | 目前董事長的姓名。 |
| 財報股本(億) | CurrentCapitalin100Million | 台股 | | 公司財報(季、年)上載明的股本，換算成億元。 |

## 使用範例

```xs
pe = GetField("本益比");
yield_ = GetField("殖利率");
if pe < 15 and yield_ > 5 then ret = 1;
```

> 欄位名稱以 xs-helper 官方文件為準
