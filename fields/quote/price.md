# Quote 價格欄位 (23)

> 用於 `GetQuote("欄位名")` 即時報價

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 開盤(日) | DailyOpen | 全商品 | 當日開盤價 |
| 最高(日) | DailyHigh | 全商品 | 當日最高價 |
| 最低(日) | DailyLow | 全商品 | 當日最低價 |
| 成交 | Last | 全商品 | 最新成交價 |
| 漲停價 | UpLimit | 台股/期貨 | 漲停上限價 |
| 跌停價 | DownLimit | 台股/期貨 | 跌停下限價 |
| 均價 | — | 全商品 | 當日均價 |
| 昨收 | YClose | 全商品 | 昨日收盤價 |
| 參考價 | RefPrice | 全商品 | 今日參考價 |
| 漲跌 | Change | 全商品 | 漲跌金額 |
| 漲幅(%) | ChangePercent | 全商品 | 漲跌幅百分比 |
| 振幅(%) | Amplitude | 全商品 | 當日振幅 |
| 開盤(夜) | NightOpen | 期貨 | 夜盤開盤價 |
| 最高(夜) | NightHigh | 期貨 | 夜盤最高價 |
| 最低(夜) | NightLow | 期貨 | 夜盤最低價 |
| 收盤(夜) | NightClose | 期貨 | 夜盤收盤價 |
| 上影線 | — | 全商品 | 上影線長度 |
| 下影線 | — | 全商品 | 下影線長度 |
| K棒實體 | — | 全商品 | K棒實體長度 |
| 昨開 | YOpen | 全商品 | 昨日開盤價 |
| 昨高 | YHigh | 全商品 | 昨日最高價 |
| 昨低 | YLow | 全商品 | 昨日最低價 |
| 前均價 | — | 全商品 | 前日均價 |

## 使用範例

```xs
high = GetQuote("DailyHigh");
low = GetQuote("DailyLow");
spread = high - low;
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
