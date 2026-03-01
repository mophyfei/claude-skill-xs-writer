# Data 籌碼-其他欄位 (44)

> 用於 `GetField("欄位名")` 歷史資料
> 散戶、大戶、內部人、董監、借券、庫藏股、當沖、現增等相關欄位

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| CB剩餘張數 | CBConversionAmount | 台(可轉債) | | 目前流通在外的CB張數（就是還沒有轉換的）季底值，每週更新。 |
| 借券張數 | SBLBorrowing | 台股 大盤 | | 借券的張數。 |
| 借券賣出張數 | SBUnits | 台股 大盤 | | 借券內實際賣出(放空)的張數。 |
| 借券賣出餘額張數 | SBRemain | 台股 大盤 | | 借券餘額張數，也就是到目前為止借券的淨張數。 |
| 借券餘額張數 | SBLbalance | 台股 大盤 | | 借券餘額張數，也就是到目前為止借券的淨張數。 |
| 內部人持股 | InsiderHodings | 美(股票) | | 依美國證券交易委員會規定公告的「FORM 4 」所計算出的持股異動內部人的總持有 |
| 內部人持股張數 | Insidersharesheld | 台股 | | 公司內部人持股張數。 |
| 內部人持股比例 | Insidersharesheldratio | 台股 | | 公司內部人持股占公司股本的比例。 |
| 內部人持股異動 | InsiderHodingsDiff | 美(股票) | | 依美國證券交易委員會規定公告的「FORM 4 」所計算出的公司內部人總異動股數。 |
| 大戶持股人數 | Bigsharesheldpeople | 台股 類股指數 | | 由集保公司所提供的指定級距以上的持股人數資料。 |
| 大戶持股張數 | Bigsharesheld | 台股 類股指數 | | 由集保公司所提供的指定級距以上的持股張數資料。 |
| 大戶持股比例 | Bigsharesheldratio | 台股 類股指數 | | 由集保公司所提供的指定級距以上的持股比例資料。 |
| 實戶買張 | Operatortotalbuy | 台股 | | 單一價格成交值介於50萬到100萬之間的合計買進張數。 |
| 實戶買賣超張數 | Operatordifference | 台股 | | 實戶買張 ─ 實戶賣張。 |
| 實戶賣張 | OperatortotalSell | 台股 | | 單一價格成交值介於50萬到100萬之間的合計賣出張數。 |
| 實質買盤比 | RealLongRatio | 台股 大盤 類股指數 | | 實質買進張數佔成交量的比例。 |
| 實質賣盤比 | RealShortRatio | 台股 大盤 類股指數 | | 實質賣出張數佔成交量的比例。 |
| 庫藏股實際買回張數 | Stockbuyvalue | 台股 | | 最新一次庫藏股公告的實際買回張數。 |
| 庫藏股申請家數 | BranchesStock | 大盤 類股指數 | | 市場目前正在實施庫藏股的家數。 |
| 庫藏股申請總市值 | StockTotalValue | 大盤 | | 市場目前正在實施庫藏股的庫藏股市值的加總。 |
| 庫藏股預計買回張數 | Stockestivalue | 台股 | | 最新一次庫藏股公告的預計買回張數。 |
| 散戶持股人數 | Retailsharesheldpeople | 台股 類股指數 | | 由集保公司所提供的指定級距以下的持股比例資料。 |
| 散戶持股張數 | Retailsharesheld | 台股 類股指數 | | 由集保公司所提供的指定級距以下的持股比例資料。 |
| 散戶持股比例 | Retailsharesheldratio | 台股 類股指數 | | 由集保公司所提供的指定級距以下的持股比例資料。 |
| 散戶買張 | Retailtotalbuy | 台股 | | 單一價格成交值小於50萬的合計買進張數。 |
| 散戶買賣超張數 | Retaildifference | 台股 | | 散戶買張 ─ 散戶賣張。 |
| 散戶賣張 | Retailtotalsell | 台股 | | 單一價格成交值小於50萬的合計賣出張數。 |
| 新產能預計量產日期 | DateOfNewProductionCapacity | 台股 | | 最近可能增加產能的預估量產日期。 |
| 機構持股 | 13FHoldings | 美(股票) | | 依美國證券交易委員會規定每季公告的「SEC Form 13F」所計算出的投資機構 |
| 機構持股比重 | 13FHoldingsRate | 美(股票) | | 依美國證券交易委員會規定每季公告的「SEC Form 13F」所計算出的投資機構 |
| 現券償還張數 | ShortSalesRS | 台股 大盤 | | 以現股方式償還融券的張數。 |
| 現增比率 | RatioofCashIncrement | 台股 | | 最新一期現金增資內每千股可認購新股的股數。 |
| 現增金額 | PriceofCashIncrement | 台股 | | 最新一期現金增資的發行總金額。 |
| 現股當沖張數 | NormalDayTrades | 台股 大盤 類股指數 | | 現股當日沖銷的張數。 |
| 現股當沖買進金額 | DayTradeBValue | 台股 大盤 類股指數 | | 現股當日沖銷的總買進金額。 |
| 現股當沖賣出金額 | DayTradeSValue | 台股 大盤 類股指數 | | 現股當日沖銷的總賣出金額。 |
| 現金償還張數 | POMRC | 台股 大盤 | | 以現金方式償還融資的張數。 |
| 申報人數 | DTPeople | 大盤 類股指數 | | 內部人申報轉讓持股的人數加總。 |
| 申報家數 | DTBranches | 大盤 類股指數 | | 內部人申報轉讓持股的家數加總。 |
| 申報總市值 | DTTotalValue | 大盤 類股指數 | | 內部人申報轉讓持股的市值加總。 |
| 當日沖銷張數 | Daytradeshares | 台股 大盤 | | 當日沖銷的總張數。計算公式：現股當沖張數＋資券互抵張數。 |
| 總持股人數 | TotalSharesHeldPeople | 台股 類股指數 台(可轉債) | | 由集保公司所提供的總持股人數。 |
| 董監持股佔股本比例 | DirectorHeld／Capital | 台股 | | 董監持股占公司股本的比例。 |
| 董監質設比例 | DSmortgageratio | 台股 | | 董監持股內質設的比例。 |

## 使用範例

```xs
insider = GetField("內部人持股張數");  // 或 GetField("Insidersharesheld")
retail = GetField("散戶買賣超張數");  // 或 GetField("Retaildifference")
```

> 欄位名稱以 xs-helper 官方文件為準
