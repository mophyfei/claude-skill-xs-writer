# Quote 常用報價欄位 (12)

> 用於 `GetQuote("欄位名")` 即時報價

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 成交 | Last | 全商品 | 最新成交價 |
| 成交時間 | DealTime | 全商品 | 最新成交時間 |
| 估計量 | EstimatedTotalVolume | 台股/大盤 | 預估總成交量 |
| 昨量 | YVolume | 全商品 | 昨日總量 |
| 參考價 | RefPrice | 全商品 | 今日參考價(平盤價) |
| 總量(日) | TotalVolume | 全商品 | 當日累計成交量 |
| 昨收 | YClose | 全商品 | 昨日收盤價 |
| 漲跌 | Change | 全商品 | 漲跌金額 |
| 漲幅(%) | ChangePercent | 全商品 | 漲跌百分比 |
| 振幅(%) | Amplitude | 全商品 | 當日振幅百分比 |
| 開盤(日) | DailyOpen | 全商品 | 當日開盤價 |
| 總額 | — | 全商品 | 當日累計成交金額 |

## 使用範例

```xs
value = GetQuote("成交");
value = GetQuote("Last");
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
