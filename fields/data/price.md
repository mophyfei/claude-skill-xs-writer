# Data 價格欄位 (14)

> 用於 `GetField("欄位名")` 歷史資料

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| 均價 | AvgPrice | 全商品 | 當日均價 |
| 上影線 | — | 全商品 | Max(High,Open)-Max(Close,Open)之差 |
| 下影線 | — | 全商品 | Min(Close,Open)-Low |
| 漲幅 | — | 全商品 | 漲跌金額 |
| 漲幅(%) | — | 全商品 | 漲跌幅百分比 |
| 振幅 | — | 全商品 | (High-Low)/前收 |
| K棒實體 | — | 全商品 | Abs(Close-Open) |
| 還原收盤價 | — | 台股 | 除權息還原價 |
| 還原開盤價 | — | 台股 | 除權息還原開盤 |
| 還原最高價 | — | 台股 | 除權息還原最高 |
| 還原最低價 | — | 台股 | 除權息還原最低 |
| 漲停價 | — | 台股/期貨 | 漲停上限價 |
| 跌停價 | — | 台股/期貨 | 跌停下限價 |
| 參考價 | — | 全商品 | 當日參考價 |

## 使用範例

```xs
// 計算上下影線比
upperShadow = GetField("上影線");
lowerShadow = GetField("下影線");
body = GetField("K棒實體");
if body > 0 then ratio = (upperShadow + lowerShadow) / body;
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
