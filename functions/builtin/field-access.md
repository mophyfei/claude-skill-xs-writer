# 欄位函數 (14)

## 資料取得

| 函數 | 說明 | 語法 |
|------|------|------|
| `GetField("欄位","頻率")` | 取得資料欄位 | `GetField("成交量","D")` |
| `GetQuote("欄位")` | 取得即時報價(僅警示/交易) | `GetQuote("成交")` |
| `GetSymbolField("商品","欄位","頻率")` | 取其他商品欄位 | `GetSymbolField("2330","收盤價","D")` |

頻率代碼：`"D"`=日, `"W"`=週, `"M"`=月, `"Q"`=季, `"Y"`=年, `"5"`=5分

## 欄位檢查

| 函數 | 說明 | 語法 |
|------|------|------|
| `CheckField("欄位","頻率")` | 檢查欄位是否有值 | `if CheckField("本益比","D") then ...` |
| `CheckSymbolField("商品","欄位","頻率")` | 檢查其他商品欄位 | `CheckSymbolField("2330","收盤價","D")` |

## 商品資訊

| 函數 | 說明 | 回傳範例 |
|------|------|---------|
| `Symbol` | 當前商品代碼 | "2330" |
| `SymbolName` | 當前商品名稱 | "台積電" |
| `SymbolType` | 商品類型 | "Stock","Future","Option" |

## 群組操作

| 函數 | 說明 | 語法 |
|------|------|------|
| `GetSymbolGroup(n)` | 取群組第 n 個商品代碼 | `GetSymbolGroup(1)` |
| `GroupSize` | 群組商品數量 | `GroupSize` |
| `SymbolCount` | 同 GroupSize | `SymbolCount` |

## 常用範例

```xs
// 取得基本面資料
_PE = GetField("本益比", "D");
_ROE = GetField("股東權益報酬率", "Q");

// 取得即時報價（僅警示/交易腳本）
_Price = GetQuote("成交");
_BidPrice = GetQuote("買進");
_AskPrice = GetQuote("賣出");

// 跨商品比較
_TSMC = GetSymbolField("2330", "收盤價", "D");
if CheckSymbolField("2330", "收盤價", "D") then
    _Ratio = Close / _TSMC;

// 安全取值（先檢查再取用）
if CheckField("本益比", "D") then
    _PE = GetField("本益比", "D");
```

注意：`GetQuote` 不可回溯，`GetQuote("成交")[1]` 是無效寫法。
