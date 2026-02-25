# XS 腳本類型限制

XS 有四種腳本類型，各有嚴格限制，**不能跨類型使用函數**。

## 1. 指標腳本 (Indicator)

- `plot` 只能定義**數值 + 名稱 + 勾選框**
- **不能**在 plot 中定義顏色、樣式、寬度（由使用者在 UI 設定）

```xs
// 正確
plot1(_MA, "均線");
plot2(_Signal, "訊號", true);  // true = 預設勾選

// 錯誤：不能指定顏色/樣式
plot1(_MA, "均線", red, solid, 2);  // 語法錯誤
```

## 2. 交易腳本 (Trading)

- 使用 `position` 查詢持倉、`filled` 查詢成交、`setposition` 下單
- **禁止**使用 `marketposition`（非 XS 語法）

```xs
// 正確
if position = 0 and _BuySignal then
    setposition(1);  // 買進

if position = 1 and _SellSignal then
    setposition(0);  // 賣出

// 錯誤
if marketposition = 1 then ...  // 不是 XS 語法
```

## 3. 選股腳本 (Selection)

- `rank` 區塊是**獨立作用域**，無法使用外部 input/var
- 排序用 `ret`，篩選用 `ranking`

```xs
input: _Period(20, "週期");
var: _Value(0);

_Value = Average(Close, _Period);
if _Value > 0 then ret = _Value;

rank:
    // 這裡無法使用 _Period 或 _Value
    if ranking <= 10 then ret = 1;
end;
```

## 4. 警示腳本 (Alert)

- **不能**使用 `OutputField`（那是選股腳本專用）
- 可使用 `GetQuote` 取即時報價

```xs
// 警示腳本用 raiseruntime 觸發
if _Condition then
    raiseruntime("訊號觸發");
```

## 跨類型限制

| 功能 | 指標 | 交易 | 選股 | 警示 |
|------|------|------|------|------|
| plot | O | X | X | X |
| PlotK | O | X | X | X |
| setposition | X | O | X | X |
| ret/ranking | X | X | O | X |
| OutputField | X | X | O | X |
| GetQuote | X | X | X | O* |
| raiseruntime | X | X | X | O |

*GetQuote 在交易腳本中也可使用，但無歷史資料。
