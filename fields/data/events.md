# Data 事件欄位 (29)

> 用於 `GetField("欄位名")` 歷史資料

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 停止轉換結束日 | StopConvertingED | 台(可轉債) | | 最近一次停止轉換結束日的日期。 |
| 停止轉換起始日 | StopConvertingSD | 台(可轉債) | | 最近一次停止轉換起始日的日期。 |
| 庫藏股結束日期 | Stockenddate | 台股 | | 最新一次庫藏股預計買回期間的結束日期。 |
| 庫藏股開始日期 | Stockstartdate | 台股 | | 最新一次庫藏股預計買回期間的開始日期。 |
| 新股上市日 | LaunchDayOfNewShares | 台股 | | 最近一次新股上市日期。 |
| 最後交易日 | LastTradeDate | 台(權證) 台(可轉債) 期貨 選擇權 | | 商品的最後交易日。欄位格式為西元年月日，例如20221101。 |
| 最後過戶日期 | LastTransferDay | 台股 | | 最新一期的除權息最後過戶日日期，以西元年月日來表示，當日期為2023年6月18日 |
| 法說會日期 | InvestorConferenceDate | 台股 | | 最新一期法說會日期。 |
| 減資新股上市日 | LaunchDayOfCapitalReduction | 台股 | | 最近一次減資的新股上市日。 |
| 減資日期 | CapitalReductionDate | 台股 | | 最近一次減資日期日期。 |
| 減資最後過戶日 | LastTransferDateOfCapitalReduction | 台股 | | 最近一次減資的最後過戶日。 |
| 減資比例 | CapitalReductionRatio | 台股 | | 最近一次減資的比例。 |
| 現增價格 | CashIncrementAmount | 台股 | | 最新一期現金增資的發行價格。 |
| 現增新股上市日 | LaunchDayOfNewSharesCashIncrement | 台股 | | 最近一次現金增資的新股上市日。 |
| 現增最後過戶日 | LastTransferDayOfCashIncrement | 台股 | | 最近一次現金增資的最後過戶日。 |
| 現增繳款日期 | DateofCashIncrement | 台股 | | 最近一次現金增資的最後繳款日。 |
| 股東會日期 | DateofMeetingofShareHolders | 台股 | | 最近一次股東會的日期。 |
| 處置結束日期 | DispositionED | 台股 台(權證) 台(可轉債) 台(特別股) | | 最近一次處置期間的結束日期。 |
| 處置開始日期 | DispositionSD | 台股 台(權證) 台(可轉債) 台(特別股) | | 最近一次處置期間的開始日期。 |
| 融券最後回補日 | ShortSaleFinalRecallDate | 台股 | | 最近一次融券最後回補日的日期。 |
| 除息值 | ExDividendValue | 台股 | | 最近一次公佈的除息值。 |
| 除息年度 | ExDividendYear | 台(股票) | | 最近一次公佈的除息資料所對應的股息所屬年度。 |
| 除息日期 | ExDividendDate | 台股 | | 最近一次公佈的除息日期。 |
| 除權值 | ExRightValue | 台股 | | 最近一次公佈的除權值。 |
| 除權年度 | ExRightYear | 台(股票) | | 最近一次公佈的除權資料所對應的股利所屬年度。 |
| 除權息值 | ExDividendRightValue | 台股 | | 最近一次公佈的除權或是除息的數值。 |
| 除權息年度 | ExDividendRightYear | 台(股票) | | 最近一次公佈的除權或是除息資料所對應的股利或是股息所屬年度。 |
| 除權息日期 | ExDividendRightDate | 台股 | | 最近一次公佈的除權或是除息日期。 |
| 除權日期 | ExRightDate | 台股 | | 最近一次公佈的除權日期。 |

## 使用範例

```xs
exDate = GetField("除權息日期");  // 或 GetField("ExDividendRightDate")
div = GetField("除息值");  // 或 GetField("ExDividendValue")
```

> 欄位名稱以 xs-helper 官方文件為準
