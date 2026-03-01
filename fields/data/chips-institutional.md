# Data 籌碼-法人欄位 (53)

> 用於 `GetField("欄位名")` 歷史資料
> 外資、投信、自營商、法人相關欄位

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 外資成本 | FBSCost | 台股 | | 系統估算的外資持股成本。 |
| 外資持股 | Fsharesheld | 台股 類股指數 | | 外資持有的張數。 |
| 外資持股比例 | Fsharesheldratio | 台股 | | 外資持股的比例。 |
| 外資買張 | Ftotalbuy | 台股 | | 外資買進張數。 |
| 外資買賣超 | Fdifference | 台股 大盤 類股指數 | | 外資買賣超。數值內容/單位依商品類型而異。 |
| 外資買賣超張數 | FdifferenceonStock | 台股 類股指數 | | 外資買賣超張數。 |
| 外資買賣超金額 | FBSAmount | 大盤 | | 外資買賣超金額，計算公式為外資買進金額 ─ 外資賣出金額。 |
| 外資買進金額 | FBAmount | 大盤 | | 外資買進金額。 |
| 外資賣出金額 | FSAmount | 大盤 | | 外資賣出金額。 |
| 外資賣張 | Ftotalsell | 台股 | | 外資賣出張數。 |
| 投信成本 | SBSCost | 台股 | | 系統估算的投信持股成本。 |
| 投信持股 | Ssharesheld | 台股 類股指數 | | 系統估計值，計算方式是累計長期的投信買賣超張數。 |
| 投信持股比例 | Ssharesheldratio | 台股 | | 系統估算值，計算公式為：投信持股/流通在外張數 \* 100%。 |
| 投信買張 | Stotalbuy | 台股 | | 投信買進張數。 |
| 投信買賣超 | Sdifference | 台股 大盤 類股指數 | | 投信買賣超。數值內容/單位依商品類型而異。 |
| 投信買賣超張數 | SdifferenceonStock | 台股 類股指數 | | 投信買賣超張數。 |
| 投信買賣超金額 | SBSAmount | 大盤 | | 投信買賣超金額，計算公式為投信買進金額 ─ 投信賣出金額。 |
| 投信買進金額 | SBAmount | 大盤 | | 投信買進金額。 |
| 投信賣出金額 | SSAmount | 大盤 | | 投信賣出金額。 |
| 投信賣張 | Stotalsell | 台股 | | 投信賣出張數。 |
| 法人持股 | InvestorSharesHeld | 台股 類股指數 | | 三大法人(外資、投信、自營商)合計估計持股張數。 |
| 法人持股比例 | InvestorSharesHeldRatio | 台股 | | 系統估算值，計算公式為：法人持股/流通在外張數 \* 100%。 |
| 法人買張 | InvestorTotalBuy | 台股 | | 三大法人(外資、投信、自營商)合計買進張數。 |
| 法人買賣超 | InvestorDifferenceTotal | 台股 大盤 類股指數 | | 三大法人買賣超。數值內容/單位依商品類型而異。 |
| 法人買賣超張數 | InvestorDifference | 台股 類股指數 | | 三大法人(外資、投信、自營商)合計買賣超張數。 |
| 法人買賣超金額 | InvestorDifferenceAmount | 大盤 | | 三大法人(外資、投信、自營商)合計買賣超金額。 |
| 法人買進比重 | InvestorLongRatio | 大盤 | | 法人買進金額占大盤成交量的比重。 |
| 法人買進金額 | InvestorTotalBuyAmount | 大盤 | | 三大法人(外資、投信、自營商)合計買進金額。 |
| 法人賣出比重 | InvestorShortRatio | 大盤 | | 法人賣出金額占大盤成交量的比重。 |
| 法人賣出金額 | InvestorTotalSellAmount | 大盤 | | 三大法人(外資、投信、自營商)合計賣出金額。 |
| 法人賣張 | InvestorTotalSell | 台股 | | 三大法人(外資、投信、自營商)合計賣出張數。 |
| 自營商成本 | DBSCost | 台股 | | 系統估算的自營商持股成本。 |
| 自營商持股 | Dsharesheld | 台股 類股指數 | | 系統估計值，計算方式是累計長期的自營商買賣超張數。 |
| 自營商持股比例 | Dsharesheldratio | 台股 | | 系統估算值，計算公式為：自營商持股/流通在外張數 \* 100%。 |
| 自營商自行買賣買張 | DSelftotalbuy | 台股 大盤 | | 自營商買進張數內歸屬於自行買賣的數量。 |
| 自營商自行買賣買賣超 | DSelfdifference | 台股 大盤 | | 自營商買賣超內歸屬於自行買賣的數量。數值內容/單位依商品類型而異。 |
| 自營商自行買賣買賣超金額 | DSelfDifferenceAmount | 大盤 | | 計算公式為自營商自行買賣買進金額 ─ 自營商自行買賣賣出金額。 |
| 自營商自行買賣買進金額 | DSelfTotalBuyAmount | 大盤 | | 自營商買進金額內歸屬於自行買賣的數量。 |
| 自營商自行買賣賣出金額 | DSelfTotalSellAmount | 大盤 | | 自營商賣出金額內歸屬於自行買賣的數量。 |
| 自營商自行買賣賣張 | DSelftotalsell | 台股 大盤 | | 自營商買進張數內歸屬於自行買賣的數量。 |
| 自營商買張 | Dtotalbuy | 台股 | | 自營商買進張數。 |
| 自營商買賣超 | Ddifference | 台股 大盤 類股指數 | | 自營商買賣超。數值內容/單位依商品類型而異。 |
| 自營商買賣超張數 | DdifferenceonStock | 台股 類股指數 | | 自營商買賣超張數。 |
| 自營商買賣超金額 | DBSAmount | 大盤 | | 自營商買賣超金額，計算公式為自營商買進金額 ─ 自營商賣出金額。 |
| 自營商買進金額 | DBAmount | 大盤 | | 自營商買進金額。 |
| 自營商賣出金額 | DSAmount | 大盤 | | 自營商賣出金額。 |
| 自營商賣張 | Dtotalsell | 台股 | | 自營商賣出張數。 |
| 自營商避險買張 | DtotalHedgebuy | 台股 大盤 | | 自營商買進張數內歸屬於避險的數量。 |
| 自營商避險買賣超 | DHedgedifference | 台股 大盤 | | 自營商買賣超內歸屬於避險的數量。數值內容/單位依商品類型而異。 |
| 自營商避險買賣超金額 | DHedgeDifferenceAmount | 大盤 | | 計算公式為自營商避險買進金額 ─ 自營商避險賣出金額。 |
| 自營商避險買進金額 | DTotalHedgeBuyAmount | 大盤 | | 自營商買進金額內歸屬於避險的數量。 |
| 自營商避險賣出金額 | DTotalHedgeSellAmount | 大盤 | | 自營商賣出金額內歸屬於避險的數量。 |
| 自營商避險賣張 | DtotalHedgesell | 台股 大盤 | | 自營商買進張數內歸屬於避險的數量。 |

## 使用範例

```xs
fBuy = GetField("外資買賣超");  // 或 GetField("Fdifference")
iTrust = GetField("投信買賣超");  // 或 GetField("Sdifference")
dealer = GetField("自營商買賣超");  // 或 GetField("Ddifference")
```

> 欄位名稱以 xs-helper 官方文件為準
