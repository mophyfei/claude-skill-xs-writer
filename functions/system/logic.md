# 邏輯判斷 (13)

## 交叉判斷

| 函數 | 說明 | 語法 |
|------|------|------|
| `CrossOver(a,b)` | a 上穿 b（金叉） | `CrossOver(MA5,MA20)` |
| `CrossUnder(a,b)` | a 下穿 b（死叉） | `CrossUnder(MA5,MA20)` |

等價寫法：`CrossOver(a,b)` 等同 `a cross over b`

## 條件統計

| 函數 | 說明 | 語法 |
|------|------|------|
| `CountIf(cond,period)` | N期內條件成立次數 | `CountIf(Close>Open,20)` |
| `AverageIF(cond,data,period)` | 條件成立時的平均 | `AverageIF(Close>Open,Close,20)` |
| `SummationIf(cond,data,period)` | 條件成立時的加總 | `SummationIf(Close>Open,Volume,20)` |
| `MinIF(cond,data,period)` | 條件成立時的最小值 | `MinIF(Close>Open,Low,20)` |
| `MaxIF(cond,data,period)` | 條件成立時的最大值 | `MaxIF(Close>Open,High,20)` |

## 條件取值

| 函數 | 說明 | 語法 |
|------|------|------|
| `IFF(cond,trueVal,falseVal)` | 條件運算式 | `IFF(Close>Open,1,-1)` |

等價寫法：`IFF(c,t,f)` 類似 `if c then t else f`，但可用在運算式中。

## 信號過濾

| 函數 | 說明 | 語法 |
|------|------|------|
| `Filter(cond,period)` | 信號過濾(冷卻期) | `Filter(CrossOver(MA5,MA20),10)` |

Filter 在條件首次成立後，後續 period 根 K 棒內不再觸發。

## 常用範例

```xs
// 金叉死叉
if CrossOver(EMA(Close,12), EMA(Close,26)) then
    Alert("EMA 金叉");
if CrossUnder(EMA(Close,12), EMA(Close,26)) then
    Alert("EMA 死叉");

// 20日內上漲天數
_UpDays = CountIf(Close > Open, 20);
_UpRatio = _UpDays / 20 * 100;

// 上漲日的平均成交量
_UpVolAvg = AverageIF(Close > Open, Volume, 20);

// 條件取值（單行寫法）
_Direction = IFF(Close > Average(Close,20), 1, -1);

// 信號過濾：金叉後10根不重複觸發
_Signal = Filter(CrossOver(MA5, MA20), 10);
if _Signal then SetPosition(1000);

// 紅K比例選股
_RedRatio = CountIf(Close > Open, 20) / 20 * 100;
if _RedRatio >= 70 then
    OutputField1(_RedRatio, "紅K比例%");
```
