# Selection 籌碼-主力/其他欄位 (71)

> 用於選股腳本
> 主力、控盤者、散戶、大戶、內部人、董監、借券、庫藏股、當沖等相關欄位

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| CB剩餘張數 | CBConversionAmount | 台(可轉債) | | 目前流通在外的CB張數（就是還沒有轉換的）季底值，每週更新。 |
| ETF規模 | ETFSize | 台股 美(ETF) | | ETF的規模，單位是元/美元. |
| 主力平均買超成本 | AvgCostLeadertotalbuy | 台股 | | 前十五大買超券商的買超成本。 |
| 主力平均賣超成本 | AvgCostLeadertotalSell | 台股 | | 前十五大賣超券商的賣超成本。 |
| 主力成本 | LeaderCost | 台股 | | 系統估計的長期主力持股成本。 |
| 主力持股 | LeaderSharesHeld | 台股 | | 系統估計的長期主力持股數量。 |
| 主力買張 | Leadertotalbuy | 台股 | | 前十五大買超分點的買超張數加總。 |
| 主力買賣超張數 | LeaderDifference | 台股 | | 主力買張 ─ 主力賣張。 |
| 主力賣張 | Leadertotalsell | 台股 | | 前十五大賣超分點的賣超張數加總。 |
| 借券張數 | SBLBorrowing | 台股 | | 借券的張數。 |
| 借券賣出張數 | SBUnits | 台股 | | 借券內實際賣出(放空)的張數。 |
| 借券賣出餘額張數 | SBRemain | 台股 | | 借券餘額張數，也就是到目前為止借券的淨張數。 |
| 借券餘額張數 | SBLbalance | 台股 | | 借券餘額張數，也就是到目前為止借券的淨張數。 |
| 內部人持股 | InsiderHodings | 美(股票) | | 依美國證券交易委員會規定公告的「FORM 4 」所計算出的持股異動內部人的總持有 |
| 內部人持股張數 | Insidersharesheld | 台股 | | 內部人= 台灣經濟新報所提供的所有董監持股資料 – 大股東。不重複計算股數 (即 |
| 內部人持股比例 | Insidersharesheldratio | 台股 | | 公司內部人持股占公司股本的比例。 |
| 內部人持股異動 | InsiderHodingsDiff | 美(股票) | | 依美國證券交易委員會規定公告的「FORM 4 」所計算出的公司內部人總異動股數。 |
| 公積及其他佔股本比重 | CapitalReserveOther／Capital | 台股 | | 股本形成中，公積及其他來源所佔的比重。 |
| 分公司交易家數 | BranchesOfTraded | 台股 類股指數 | | 統計有買進或是賣出的券商分點家數。 |
| 分公司淨買超金額家數 | BranchesOfNetBuyers | 台股 類股指數 | | 統計買超的券商分點家數。 |
| 分公司淨賣超金額家數 | BranchesOfNetSellers | 台股 類股指數 | | 統計賣超的券商分點家數。 |
| 分公司買進家數 | LongBranches | 台股 | | 統計買進金額大於零的券商分點家數。 |
| 分公司賣出家數 | ShortBranches | 台股 | | 統計賣出金額大於零的券商分點家數。 |
| 吉尼係數 | GiniCoefficient | 台股 | | 使用券商分點交易比重所推估出來的吉尼系統。 |
| 地緣券商買賣超張數 | GBDifference | 台股 類股指數 | | 「地緣券商」的買進張數 － 賣出張數。 |
| 大戶持股人數 | Bigsharesheldpeople | 台股 類股指數 | | 由集保公司所提供的指定級距以上的持股人數資料。 |
| 大戶持股張數 | Bigsharesheld | 台股 類股指數 | | 由集保公司所提供的指定級距以上的持股張數資料。 |
| 大戶持股比例 | Bigsharesheldratio | 台股 類股指數 | | 由集保公司所提供的指定級距以上的持股比例資料。 |
| 官股券商買賣超張數 | OBDifference | 台股 類股指數 | | 「官股券商」買進張數 - 賣出張數。 |
| 實戶買張 | operatortotalbuy | 台股 | | 單一價格成交值介於50萬到100萬之間的合計買進張數。 |
| 實戶買賣超張數 | operatordifference | 台股 | | 實戶買張 ─ 實戶賣張。 |
| 實戶賣張 | operatortotalSell | 台股 | | 單一價格成交值介於50萬到100萬之間的合計賣出張數。 |
| 實質買盤比 | RealLongRatio | 台股 類股指數 | | 實質買進張數佔成交量的比例。 |
| 實質賣盤比 | RealShortRatio | 台股 | | 實質賣出張數佔成交量的比例。 |
| 庫藏股實際買回張數 | Stockbuyvalue | 台股 | | 最新一次庫藏股公告的實際買回張數。 |
| 庫藏股預計買回張數 | Stockestivalue | 台股 | | 最新一次庫藏股公告的預計買回張數。 |
| 控盤者成本線 | CostLine | 台股 | | 系統估計的控盤者的持股成本。 |
| 控盤者買張 | controllertotalbuy | 台股 | | 單一價格成交值大於100萬的合計買進張數。 |
| 控盤者買賣超張數 | controllerdifference | 台股 | | 控盤者買張 ─ 控盤者賣張。 |
| 控盤者賣張 | controllertotalsell | 台股 | | 單一價格成交值大於100萬的合計賣出張數。 |
| 散戶持股人數 | Retailsharesheldpeople | 台股 類股指數 | | 由集保公司所提供的指定級距以下的持股比例資料。 |
| 散戶持股張數 | Retailsharesheld | 台股 類股指數 | | 由集保公司所提供的指定級距以下的持股比例資料。 |
| 散戶持股比例 | Retailsharesheldratio | 台股 類股指數 | | 由集保公司所提供的指定級距以下的持股比例資料。 |
| 散戶買張 | retailtotalbuy | 台股 | | 單一價格成交值小於50萬的合計買進張數。 |
| 散戶買賣超張數 | retaildifference | 台股 | | 散戶買張 ─ 散戶賣張。 |
| 散戶賣張 | retailtotalsell | 台股 | | 單一價格成交值小於50萬的合計賣出張數。 |
| 機構持股 | 13FHoldings | 美(股票) | | 依美國證券交易委員會規定每季公告的「SEC Form 13F」所計算出的投資機構 |
| 機構持股比重 | 13FHoldingsRate | 美(股票) | | 依美國證券交易委員會規定每季公告的「SEC Form 13F」所計算出的投資機構 |
| 現券償還張數 | ShortSalesRS | 台股 | | 以現股方式償還融券的張數。 |
| 現股當沖張數 | NormalDayTrades | 台股 類股指數 | | 現股當日沖銷的張數。 |
| 現股當沖買進金額 | DayTradeBValue | 台股 類股指數 | | 現股當日沖銷的總買進金額。 |
| 現股當沖賣出金額 | DayTradeSValue | 台股 類股指數 | | 現股當日沖銷的總賣出金額。 |
| 現金償還張數 | POMRC | 台股 | | 以現金方式償還融資的張數。 |
| 現金增資佔股本比重 | CashIncrease／Capital | 台股 | | 股本形成中，現金增資所佔的比重。 |
| 當日沖銷張數 | Daytradeshares | 台股 | | 當日沖銷的總張數。計算公式：現股當沖張數＋資券互抵張數。 |
| 盈餘轉增資佔股本比重 | CaptialIncreaseFromEarning／Capital | 台股 | | 股本形成中，盈餘轉增資所佔的比重。 |
| 籌碼鎖定率 | RatioOfMajorHolder | 台股 | | 計算公式: 主力券商買超張數／(發行張數－董監持股張數) \* 100%。 |
| 綜合前十大券商買賣超張數 | IB10Difference | 台股 類股指數 | | 「綜合前十大券商」買進張數 － 賣出張數。 |
| 總持股人數 | TotalSharesHeldPeople | 台股 類股指數 | | 由集保公司所提供的總持股人數。 |
| 股票基金持有檔數 | HoldingByFunds | 台股 | | 根據主管機關核准的境內外共同基金，每季公告的占基金淨資產價值1%以上持股資料做統 |
| 董監持股 | DirectorHeld | 台股 類股指數 | | 董事與監察人的持股張數。 |
| 董監持股佔股本比例 | DirectorHeld／Capital | 台股 | | 董監持股占公司股本的比例。 |
| 董監質設比例 | DSmortgageratio | 台股 | | 董監持股內質設的比例。 |
| 買家數 | NetLongBranches | 台股 類股指數 | | 統計買超張數大於零的券商家數。 |
| 買進公司家數 | LongSecurityFirms | 台股 | | 統計買進金額大於零的券商家數。 |
| 賣出公司家數 | ShortSecurityFirms | 台股 | | 統計賣出金額大於零的券商家數。 |
| 賣家數 | NetShortBranches | 台股 類股指數 | | 統計賣超張數大於零的券商家數。 |
| 關聯券商買賣超張數 | CorrelationBrokerDifference | 台股 | | 「關聯券商」買進張數 － 賣出張數。 |
| 關鍵券商買賣超張數 | KeyBrokerDifference | 台股 類股指數 | | 「關鍵券商」買進張數 － 賣出張數。 |
| 集保張數 | SharesUnderCentralCustody | 台股 | | 由集保公司所提供的集保張數，換算成萬張。 |
| 集保張數佔發行張數百分比 | SharesUnderCentralCustody％ | 台股 | | 計算公式 : 集保張數／發行張數 \*100%。 |

## 使用範例

```xs
major = GetField("主力買賣超張數");
if major > 1000 then ret = 1;
```

> 欄位名稱以 xs-helper 官方文件為準
