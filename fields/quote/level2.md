# Quote 五檔統計欄位 (28)

> 用於 `GetQuote("欄位名")` 即時五檔報價

## 委買價 (5)

| 欄位名稱 | English Code | 備註 |
|----------|-------------|------|
| 委買1 | BidPrice1 | 最佳買價 |
| 委買2 | BidPrice2 | 第二檔買價 |
| 委買3 | BidPrice3 | 第三檔買價 |
| 委買4 | BidPrice4 | 第四檔買價 |
| 委買5 | BidPrice5 | 第五檔買價 |

## 委賣價 (5)

| 欄位名稱 | English Code | 備註 |
|----------|-------------|------|
| 委賣1 | AskPrice1 | 最佳賣價 |
| 委賣2 | AskPrice2 | 第二檔賣價 |
| 委賣3 | AskPrice3 | 第三檔賣價 |
| 委賣4 | AskPrice4 | 第四檔賣價 |
| 委賣5 | AskPrice5 | 第五檔賣價 |

## 委買量 (5)

| 欄位名稱 | English Code | 備註 |
|----------|-------------|------|
| 委買量1 | BidVolume1 | 最佳買量 |
| 委買量2 | BidVolume2 | — |
| 委買量3 | BidVolume3 | — |
| 委買量4 | BidVolume4 | — |
| 委買量5 | BidVolume5 | — |

## 委賣量 (5)

| 欄位名稱 | English Code | 備註 |
|----------|-------------|------|
| 委賣量1 | AskVolume1 | 最佳賣量 |
| 委賣量2 | AskVolume2 | — |
| 委賣量3 | AskVolume3 | — |
| 委賣量4 | AskVolume4 | — |
| 委賣量5 | AskVolume5 | — |

## 彙總 (4)

| 欄位名稱 | English Code | 備註 |
|----------|-------------|------|
| 總委買 | TotalBidVolume | 五檔委買合計 |
| 總委賣 | TotalAskVolume | 五檔委賣合計 |
| 委買筆1~5 | BidCount1~5 | 各檔委買筆數(台股) |
| 委賣筆1~5 | AskCount1~5 | 各檔委賣筆數(台股) |

## 使用範例

```xs
spread = GetQuote("AskPrice1") - GetQuote("BidPrice1");
bidTotal = GetQuote("TotalBidVolume");
```

> 完整欄位清單請查閱 xs-helper: ~/.cache/xs-helper/xs-helper backup/
