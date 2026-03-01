# Data 籌碼-主力/券商欄位 (38)

> 用於 `GetField("欄位名")` 歷史資料
> 主力、控盤者、券商、買賣力等相關欄位

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 主力成本 | LeaderCost | 台股 | | 系統估計的長期主力持股成本。 |
| 主力持股 | Leadersharesheld | 台股 類股指數 | | 系統估計的長期主力持股數量。 |
| 主力累計買賣超金額 | MBSCumAmount | 大盤 | | 累計的主力買賣超金額。 |
| 主力買張 | Leadertotalbuy | 台股 | | 前十五大買超分點的買超張數加總。 |
| 主力買賣超張數 | LeaderDifference | 台股 類股指數 | | 主力買張 ─ 主力賣張。 |
| 主力買進金額 | MBAmount | 大盤 | | 前十五大買超分點的買超金額合計。 |
| 主力賣出金額 | MSAmount | 大盤 | | 前十五大賣超分點的賣超金額合計。 |
| 主力賣張 | Leadertotalsell | 台股 | | 前十五大賣超分點的賣超張數加總。 |
| 主動性交易比重 | ActTradeRatio | 台股 | | 控盤者的主動買盤+主動賣盤佔淨成交張數的比重。 |
| 主動買力 | ActLongForce | 台股 | | 控盤者的主動買盤佔淨成交張數的比重。 |
| 主動賣力 | ActShortForce | 台股 | | 控盤者的主動賣盤佔淨成交張數的比重。 |
| 分公司交易家數 | BranchesOfTrading | 台股 類股指數 | | 統計有買進或是賣出的券商分點家數。 |
| 分公司淨買超金額家數 | BranchesOfNetBought | 台股 類股指數 | | 統計買超的券商分點家數。 |
| 分公司淨賣超金額家數 | BranchesOfNetSold | 台股 類股指數 | | 統計賣超的券商分點家數。 |
| 分公司買進家數 | LongBranches | 台股 | | 統計買進金額大於零的券商分點家數。 |
| 分公司賣出家數 | ShortBranches | 台股 | | 統計賣出金額大於零的券商分點家數。 |
| 吉尼係數 | GiniCoefficient | 台股 | | 使用券商分點交易比重所推估出來的吉尼系統。 |
| 地緣券商買賣超張數 | GBDifference | 台股 類股指數 | | 「地緣券商」的買進張數 － 賣出張數。 |
| 官股券商累計買賣超金額 | OBBSCumAmount | 大盤 | | 「官股券商」每日買賣超金額的累積值。 |
| 官股券商買賣超張數 | OBDifference | 台股 類股指數 | | 「官股券商」買進張數 - 賣出張數。 |
| 官股券商買進金額 | OBBAmount | 台股 大盤 | | 「官股券商」對市場所有股票的合計買進金額。 |
| 官股券商賣出金額 | OBSAmount | 台股 大盤 | | 「官股券商」對市場所有股票的合計賣出金額。 |
| 市場總分點數 | TotalBranches | 台股 | | 市場所有的券商分點家數。 |
| 控盤者成本線 | CostLine | 台股 | | 系統估計的控盤者的持股成本。 |
| 控盤者買張 | Controllertotalbuy | 台股 | | 單一價格成交值大於100萬的合計買進張數。 |
| 控盤者買賣超張數 | Controllerdifference | 台股 | | 控盤者買張 ─ 控盤者賣張。 |
| 控盤者賣張 | Controllertotalsell | 台股 | | 單一價格成交值大於100萬的合計賣出張數。 |
| 收集派發指標 | ADIndicator | 台股 | | 分公司賣出家數 － 分公司買進家數。 |
| 綜合前十大券商累計買賣超金額 | IB10BSCumAmount | 大盤 | | 「綜合前十大券商」每日買賣超金額的累積值。 |
| 綜合前十大券商買賣超張數 | IB10Difference | 台股 類股指數 | | 「綜合前十大券商」買進張數 － 賣出張數。 |
| 綜合前十大券商買進金額 | IB10BAmount | 大盤 | | 「綜合前十大券商」對市場所有股票的合計買進金額。 |
| 綜合前十大券商賣出金額 | IB10SAmount | 大盤 | | 「綜合前十大券商」對市場所有股票的合計賣出金額。 |
| 買家數 | NetLongBranches | 台股 | | 統計買超張數大於零的券商家數。 |
| 買進公司家數 | LongSecurityFirms | 台股 | | 統計買進金額大於零的券商家數。 |
| 賣出公司家數 | ShortSecurityFirms | 台股 | | 統計賣出金額大於零的券商家數。 |
| 賣家數 | NetShortBranches | 台股 | | 統計賣超張數大於零的券商家數。 |
| 關聯券商買賣超張數 | CorrelationBrokerDifference | 台股 | | 「關聯券商」買進張數 － 賣出張數。 |
| 關鍵券商買賣超張數 | KeyBrokerDifference | 台股 類股指數 | | 「關鍵券商」買進張數 － 賣出張數。 |

## 使用範例

```xs
major = GetField("主力買賣超張數");  // 或 GetField("LeaderDifference")
cost = GetField("主力成本");  // 或 GetField("LeaderCost")
```

> 欄位名稱以 xs-helper 官方文件為準
