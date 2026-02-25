# GetField / GetQuote / GetSymbolField 完整語法

## 三大函數比較

| 特性 | GetField | GetQuote | GetSymbolField |
|------|----------|----------|----------------|
| 用途 | 本商品跨頻率欄位 | 即時報價 | 跨商品欄位 |
| 歷史資料 | 有 | **無** | 有 |
| 可用腳本 | 全部 | 警示/交易 | 全部 |
| 頻率切換 | 支援 | N/A | 支援 |

## GetField 語法

```xs
GetField("欄位名稱")
GetField("欄位名稱", "頻率")
GetField("欄位名稱", "頻率", Adjusted:=true, Default:=0)
```

### 頻率代碼一覽
| 代碼 | 說明 |
|------|------|
| `"1 Tick"` | 逐筆 |
| `"1"` `"5"` `"10"` `"15"` `"30"` `"60"` `"120"` `"240"` | 分鐘 K |
| `"D"` | 日 K |
| `"W"` `"M"` | 週 K / 月 K |
| `"Q"` `"H"` `"Y"` | 季 K / 半年 K / 年 K |
| `"AD"` `"AW"` `"AM"` | 還原日 K / 還原週 K / 還原月 K |

### 範例
```xs
// 取日線收盤價
value1 = GetField("收盤價", "D");

// 取週線成交量（還原）
value2 = GetField("成交量", "AW", Adjusted:=true);

// 取 60 分 K 最高價，預設值 0
value3 = GetField("最高價", "60", Default:=0);

// 取同頻率（不指定頻率）
value4 = GetField("外資買賣超(張)");
```

## GetQuote 語法（僅限警示/交易腳本）

```xs
GetQuote("欄位名稱")
```

- **無歷史資料**，只有當下即時值，不能用 `[1]` 回溯
- 支援 `q_` 前綴快捷欄位

```xs
// 完整寫法
value1 = GetQuote("成交價");
value2 = GetQuote("漲跌幅(%)");

// q_ 快捷寫法
value1 = q_Close;
value2 = q_DiffRate;
```

## GetSymbolField 語法

```xs
GetSymbolField("商品代碼", "欄位名稱")
GetSymbolField("商品代碼", "欄位名稱", "頻率")
```

### 商品代碼格式
```xs
// 個股
GetSymbolField("2330", "收盤價", "D")

// 指數
GetSymbolField("TSE.TW", "收盤價")

// 期貨（近月）
GetSymbolField("Future*1", "收盤價")

// 標的（選擇權用）
GetSymbolField("Underlying", "收盤價")
```

### 範例：比較個股與大盤
```xs
var: _StockReturn(0);
var: _MarketReturn(0);

_StockReturn = (Close - Close[1]) / Close[1] * 100;
_MarketReturn = (GetSymbolField("TSE.TW","收盤價","D")
                - GetSymbolField("TSE.TW","收盤價","D")[1])
                / GetSymbolField("TSE.TW","收盤價","D")[1] * 100;

plot1(_StockReturn - _MarketReturn, "超額報酬");
```
