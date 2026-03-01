# Data 市場統計欄位 (18)

> 用於 `GetField("欄位名")` 歷史資料
> 適用於大盤指數商品

| 欄位名稱 | English Code | 支援商品 | 備註 |
|----------|-------------|---------|------|
| TW50KD多空家數 | TW50KDLongShortSecurities | 大盤 | | 統計台灣50成分股內，目前K > D的家數。 |
| TW50MTM多空家數 | TW50MTMLongShortSecurities | 大盤 | | 統計台灣50成分股內，Momentum(10) > 0的家數。 |
| TW50上昇趨勢家數 | TW50UpTrendSecurities | 大盤 | | 統計台灣50成份股內趨勢向上的家數。 |
| TW50價格上漲家數 | TW50PriceUpSecurities | 大盤 | | 統計台灣50成份股內，目前這一分鐘收盤價大於前一分鐘收盤價的家數。 |
| TW50創新低家數 | TW50NewLowSecurities | 大盤 | | 統計台灣50成分股，目前這1分鐘的最低價小於最近20分鐘最低價的家數。 |
| TW50創新高家數 | TW50NewHighSecurities | 大盤 | | 統計台灣50成分股，目前這1分鐘的最高價大於最近20分鐘最高價的家數。 |
| TW50均線多空家數 | TW50MALongShortSecurities | 大盤 | | 統計台灣50成分股內，目前收盤價大於前10分鐘均價的家數。 |
| TW50大單成交次數 | TW50BidTickCountXL | 大盤 | | 加總台灣50成分股每檔商品最近10分鐘的買進大單+買進特大單的平均次數。 |
| TW50大單買進金額 | TW50BidVolumePriceXLTrend | 大盤 | | 加總台灣50成分股每檔商品的分鐘買進大單+買進特大單的金額。 |
| TW50大戶買賣力 | TW50BigSharesBidAskPower | 大盤 | | 回傳台灣50成分股每檔商品當根K棒的大戶買賣力金額。 |
| TW50紅K家數 | TW50BullKSecurities | 大盤 | | 統計台灣50成分股內，目前這1分鐘是紅K棒的家數。 |
| 上漲家數 | UpSecurities | 大盤 類股指數 | | 指數成分股內目前上漲的家數。 |
| 下跌家數 | DownSecurities | 大盤 類股指數 | | 指數成分股內目前下跌的家數。 |
| 內盤家數 | BidSecurities | 大盤 類股指數 | | 指數成分股內目前以內盤成交的家數。 |
| 外盤家數 | AskSecurities | 大盤 類股指數 | | 指數成分股內目前以外盤成交的家數。 |
| 漲停家數 | UpLimitSecs | 大盤 類股指數 | | 指數成分股內目前漲停的家數。 |
| 跌停家數 | DownLimitSecs | 大盤 類股指數 | | 指數成分股內目前跌停的家數。 |
| 騰落指標 | UDIndicator | 大盤 類股指數 | | 長期累積的(上漲家數─下跌家數)的數值。 |

## 使用範例

```xs
up = GetField("上漲家數");
down = GetField("下跌家數");
```

> 欄位名稱以 xs-helper 官方文件為準
