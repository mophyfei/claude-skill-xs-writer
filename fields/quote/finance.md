# Quote 財務欄位 (10) - 僅台股

> 用於 `GetQuote("欄位名")` 即時報價

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 每股盈餘 | EPS | 台股 | 最近四季合計 |
| 每股淨值 | BookValue | 台股 | 最近一季 |
| 股東權益報酬率 | ROE | 台股 | 最近四季合計 |
| 毛利率 | GrossMargin | 台股 | 最近一季(%) |
| 營業利益率 | OperatingMargin | 台股 | 最近一季(%) |
| 稅前淨利率 | PreTaxMargin | 台股 | 最近一季(%) |
| 負債比率 | DebtRatio | 台股 | 最近一季(%) |
| 流動比率 | CurrentRatio | 台股 | 最近一季(%) |
| 速動比率 | QuickRatio | 台股 | 最近一季(%) |
| 利息保障倍數 | InterestCoverage | 台股 | 最近四季合計 |

## 使用範例

```xs
// 取得即時報價的本益比相關數據
eps = GetQuote("每股盈餘");
price = GetQuote("成交");
if eps > 0 then pe = price / eps;
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
