# 陣列函數 (9)

## 函數列表

| 函數 | 說明 | 語法 |
|------|------|------|
| `Array_Sort(arr, size, asc)` | 排序陣列 | `Array_Sort(myArr, 10, true)` |
| `Array_Sum(arr, size)` | 陣列元素加總 | `Array_Sum(myArr, 10)` |
| `Array_Copy(src, dest, size)` | 複製陣列 | `Array_Copy(srcArr, destArr, 10)` |
| `Array_GetMaxIndex(arr, size)` | 最大值的索引 | `Array_GetMaxIndex(myArr, 10)` |
| `Array_GetMinIndex(arr, size)` | 最小值的索引 | `Array_GetMinIndex(myArr, 10)` |
| `Array_Average(arr, size)` | 陣列平均值 | `Array_Average(myArr, 10)` |
| `Array_Max(arr, size)` | 陣列最大值 | `Array_Max(myArr, 10)` |
| `Array_Min(arr, size)` | 陣列最小值 | `Array_Min(myArr, 10)` |

## 參數說明

| 參數 | 說明 |
|------|------|
| `arr` | 陣列名稱 |
| `size` | 陣列大小（元素數量） |
| `asc` | 排序方向：`true`=升冪, `false`=降冪 |
| `src` | 來源陣列 |
| `dest` | 目標陣列 |

## 常用範例

```xs
// 宣告陣列
array: _Prices[20](0);

// 填入最近 20 根收盤價
var: _i(0);
for _i = 0 to 19 begin
    _Prices[_i] = Close[_i];
end;

// 取得統計值
_Avg = Array_Average(_Prices, 20);
_Max = Array_Max(_Prices, 20);
_Min = Array_Min(_Prices, 20);
_Total = Array_Sum(_Prices, 20);

// 取得最高價的位置（幾根K棒前）
_MaxIdx = Array_GetMaxIndex(_Prices, 20);

// 排序（升冪）
array: _Sorted[20](0);
Array_Copy(_Prices, _Sorted, 20);
Array_Sort(_Sorted, 20, true);

// 排序後取中位數
_Median = _Sorted[10];
```

注意：陣列索引從 0 開始。宣告語法為 `array: name[size](初始值);`
