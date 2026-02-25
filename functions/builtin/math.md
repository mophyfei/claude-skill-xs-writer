# 數學函數 (37)

## 基本運算

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `AbsValue(x)` | 絕對值 | `AbsValue(-5)` | 5 |
| `Ceiling(x)` | 無條件進位 | `Ceiling(2.3)` | 3 |
| `Floor(x)` | 無條件捨去 | `Floor(2.7)` | 2 |
| `IntPortion(x)` | 取整數部分 | `IntPortion(2.7)` | 2 |
| `FracPortion(x)` | 取小數部分 | `FracPortion(2.7)` | 0.7 |
| `Mod(x, y)` | 取餘數 | `Mod(10, 3)` | 1 |
| `Power(x, y)` | x 的 y 次方 | `Power(2, 3)` | 8 |
| `Round(x, n)` | 四捨五入到 n 位 | `Round(2.345, 2)` | 2.35 |
| `SquareRoot(x)` | 平方根 | `SquareRoot(9)` | 3 |
| `Sign(x)` | 正負號 | `Sign(-7)` | -1 |

## 比較函數

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `MaxList(a,b,...)` | 取最大值(可變參數) | `MaxList(1,5,3)` | 5 |
| `MinList(a,b,...)` | 取最小值(可變參數) | `MinList(1,5,3)` | 1 |
| `NthMaxList(n,a,b,...)` | 第 n 大值 | `NthMaxList(2,5,3,1)` | 3 |
| `NthMinList(n,a,b,...)` | 第 n 小值 | `NthMinList(2,1,3,5)` | 3 |

## 對數與指數

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `Log(x)` | 自然對數 ln(x) | `Log(2.718)` | ≈1 |
| `ExpValue(x)` | e^x | `ExpValue(1)` | ≈2.718 |

## 三角函數

| 函數 | 說明 | 範例 |
|------|------|------|
| `Sin(x)` | 正弦（弧度） | `Sin(3.14159/2)` → 1 |
| `Cos(x)` | 餘弦（弧度） | `Cos(0)` → 1 |
| `Tan(x)` | 正切（弧度） | `Tan(3.14159/4)` → 1 |
| `ArcTan(x)` | 反正切 | `ArcTan(1)` → π/4 |

## 常用範例

```xs
// 張數計算（無條件捨去）
_Lots = IntPortion(_Amount / (Close * 1000));

// 漲跌幅取絕對值
_AbsChange = AbsValue(Close - Close[1]);

// 四捨五入到小數 2 位
_RoundPrice = Round(Close * 1.05, 2);

// 取多個值中的最大最小
_Max = MaxList(High, High[1], High[2]);
_Min = MinList(Low, Low[1], Low[2]);

// 第 2 大值
_SecondHigh = NthMaxList(2, High, High[1], High[2], High[3]);
```

注意：`IntPortion` 與 `Floor` 對正數結果相同，對負數不同：
- `IntPortion(-2.7)` → -2（取整數部分）
- `Floor(-2.7)` → -3（無條件捨去）
