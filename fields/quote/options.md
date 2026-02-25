# Quote 期權欄位 (28) - 僅台(權證)/選擇權

> 用於 `GetQuote("欄位名")` 即時報價，僅適用權證及選擇權

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| Delta | Delta | 權證/選擇權 | 標的價格敏感度 |
| Gamma | Gamma | 權證/選擇權 | Delta變化率 |
| Theta | Theta | 權證/選擇權 | 時間衰減 |
| Vega | Vega | 權證/選擇權 | 波動率敏感度 |
| Rho | Rho | 權證/選擇權 | 利率敏感度 |
| 隱含波動率 | ImpliedVolatility | 權證/選擇權 | IV(%) |
| 理論價 | TheoreticalPrice | 權證/選擇權 | 模型計算理論價 |
| 內含價值 | IntrinsicValue | 權證/選擇權 | 內在價值 |
| 時間價值 | TimeValue | 權證/選擇權 | 時間價值 |
| 歷史波動率 | HistoricalVolatility | 權證/選擇權 | HV(%) |
| 槓桿比率 | Leverage | 權證 | 槓桿倍數 |
| 實質槓桿 | EffectiveLeverage | 權證 | 有效槓桿 |
| 溢價率 | Premium | 權證 | 溢價百分比(%) |
| 行使比例 | ExerciseRatio | 權證 | 權證行使比例 |
| 履約價 | StrikePrice | 權證/選擇權 | 履約價格 |
| 剩餘天數 | DaysToExpiry | 權證/選擇權 | 到期剩餘日數 |
| 到期日 | ExpiryDate | 權證/選擇權 | 到期日期 |
| 未平倉量 | OpenInterest | 選擇權 | 未平倉合約數 |
| 未平倉量變化 | OIChange | 選擇權 | 未平倉增減 |
| 標的價格 | UnderlyingPrice | 權證/選擇權 | 標的商品價格 |
| 買賣權別 | CallPut | 權證/選擇權 | Call/Put |
| 發行量 | IssuedVolume | 權證 | 權證發行量 |
| 流通在外比例 | OutstandingRatio | 權證 | 流通比(%) |
| 發行人 | Issuer | 權證 | 發行券商 |
| 收盤價(標的) | — | 權證/選擇權 | 標的昨收 |
| 價內外程度 | Moneyness | 權證/選擇權 | 價內外% |
| 結算價 | SettlementPrice | 選擇權 | 結算價格 |
| 最後結算日 | LastSettleDate | 選擇權 | 最後結算日 |

## 使用範例

```xs
// 篩選高隱含波動率的選擇權
iv = GetQuote("隱含波動率");
delta = GetQuote("Delta");
if iv > 30 AND Abs(delta) > 0.3 then ret = 1;
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
