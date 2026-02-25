# 交易函數 (28)

> **重要：XQ 沒有 `MarketPosition` 函數！請使用 `Position`。**

## 進出場函數

| 函數 | 說明 | 語法 |
|------|------|------|
| `SetPosition(shares)` | 設定部位(推薦) | `SetPosition(1000)` 做多1張 |
| `SetPosition(0)` | 平倉 | `SetPosition(0)` |
| `SetPosition(-shares)` | 做空 | `SetPosition(-1000)` |
| `Buy("name", shares)` | 買進 | `Buy("進場", 1000)` |
| `Sell("name", shares)` | 賣出 | `Sell("出場", Position)` |
| `Short("name", shares)` | 放空 | `Short("放空", 1000)` |
| `Cover("name", shares)` | 回補 | `Cover("回補", Position)` |

## 持倉查詢

| 函數 | 說明 | 範例 |
|------|------|------|
| `Position` | 目前持倉(正=多,負=空,0=無) | `if Position > 0 then ...` |
| `Filled` | 上一筆成交數量 | `if Filled > 0 then ...` |
| `FilledAvgPrice` | 成交均價 | `_Entry = FilledAvgPrice` |
| `EntryPrice` | 進場價格 | `EntryPrice` |
| `ExitPrice` | 出場價格 | `ExitPrice` |
| `IsMarketPrice` | 是否市價單 | `if IsMarketPrice then ...` |

## 委託管理

| 函數 | 說明 | 語法 |
|------|------|------|
| `Alert("msg")` | 發出警示訊息 | `Alert("觸發進場!")` |
| `CancelAllOrders` | 取消所有委託 | `CancelAllOrders;` |

## 績效統計

| 函數 | 說明 | 回傳 |
|------|------|------|
| `MaxPositionProfit` | 持倉最大獲利 | 數值 |
| `MaxPositionLoss` | 持倉最大虧損 | 數值 |
| `BarsSinceEntry` | 進場後經過K棒數 | 整數 |
| `BarsSinceExit` | 出場後經過K棒數 | 整數 |
| `TotalTrades` | 總交易次數 | 整數 |
| `NumWinTrades` | 獲利交易次數 | 整數 |
| `NumLosTrades` | 虧損交易次數 | 整數 |
| `GrossProfit` | 總獲利金額 | 數值 |
| `GrossLoss` | 總虧損金額 | 數值 |
| `NetProfit` | 淨利潤 | 數值 |

## 常用範例

```xs
// 基本進出場
if Position = 0 then begin
    if Close cross over Average(Close, 20) then
        SetPosition(1000);
end;
if Position > 0 then begin
    if Close cross under Average(Close, 20) then
        SetPosition(0);
end;

// 停損檢查
if Position > 0 and Close <= FilledAvgPrice * 0.95 then
    SetPosition(0);

// 持倉時間出場
if Position > 0 and BarsSinceEntry >= 10 then
    SetPosition(0);
```
