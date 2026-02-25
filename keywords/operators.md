# XS 運算子參考

## 比較運算子

| 運算子 | 說明 | 範例 |
|--------|------|------|
| `=` | 等於 | `if _Signal = 1 then ...` |
| `<>` | 不等於 | `if date <> date[1] then ...` |
| `>` | 大於 | `if Close > Open then ...` |
| `<` | 小於 | `if RSI(Close,14) < 30 then ...` |
| `>=` | 大於等於 | `if Volume >= 1000 then ...` |
| `<=` | 小於等於 | `if ranking <= 10 then ...` |

## 賦值運算子

`=` **同時用於賦值和比較**，由語境決定用途。

```xs
// 賦值（在獨立語句中）
_Signal = 1;
_Price = Close;

// 比較（在 if 條件中）
if _Signal = 1 then ...
if Close = Open then ...
```

**XS 沒有 `==`，不要使用。**

## 邏輯運算子

| 運算子 | 說明 | 範例 |
|--------|------|------|
| `and` | 且 | `if A > 0 and B > 0 then ...` |
| `or` | 或 | `if A > 0 or B > 0 then ...` |
| `not` | 非 | `if not _Flag then ...` |

```xs
// 複合條件
if Close > Average(Close, 20) and Volume > Average(Volume, 10) then
    _Signal = 1;

// 多條件用括號分組
if (Close > Open and Volume > 1000) or (_Signal = 1) then
    plot1(1, "買進");
```

## 算術運算子

| 運算子 | 說明 | 範例 |
|--------|------|------|
| `+` | 加 | `_Total = _A + _B;` |
| `-` | 減 | `_Change = Close - Close[1];` |
| `*` | 乘 | `_Amount = Close * Volume;` |
| `/` | 除 | `_Rate = _Change / Close[1];` |

```xs
// 漲跌幅計算
_ChangeRate = (Close - Close[1]) / Close[1] * 100;

// 注意除以零
if Close[1] > 0 then
    _Rate = (Close - Close[1]) / Close[1] * 100;
```

## 特殊運算子

### cross over / cross under（交叉）

```xs
// 黃金交叉：快線由下往上穿越慢線
if Average(Close, 5) cross over Average(Close, 20) then
    _Signal = 1;

// 死亡交叉：快線由上往下穿越慢線
if Average(Close, 5) cross under Average(Close, 20) then
    _Signal = -1;

// 價格突破
if Close cross over _Resistance then
    plot1(1, "突破");
```

### cross over / cross under 等價邏輯
```xs
// A cross over B 等同於：
// A > B and A[1] <= B[1]

// A cross under B 等同於：
// A < B and A[1] >= B[1]
```

## 字串串接

```xs
var: _Msg("");
_Msg = "價格: " + NumToStr(Close, 2) + " 量: " + NumToStr(Volume, 0);
```

- 使用 `+` 串接字串
- `NumToStr(數值, 小數位數)` 將數值轉為字串

## 運算子優先順序（由高到低）

1. `not`（邏輯非）
2. `*`, `/`（乘除）
3. `+`, `-`（加減）
4. `=`, `<>`, `>`, `<`, `>=`, `<=`（比較）
5. `and`（邏輯且）
6. `or`（邏輯或）
7. `cross over`, `cross under`（交叉）

**建議**：複雜條件一律加括號，避免優先順序問題。
