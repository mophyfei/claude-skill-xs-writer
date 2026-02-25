# Rank 區塊語法（選股腳本）

## 核心概念
選股腳本分為兩個階段：
1. **主區塊**：計算指標、設定篩選條件、用 `ret` 回傳排序值
2. **rank 區塊**：獨立作用域，用 `ranking` 依排序結果篩選

## 關鍵規則：rank 區塊是獨立作用域
- **不能**存取主區塊的 `input` 或 `var`
- **可以**宣告同名變數，但它們是完全不同的變數
- `ranking` 是系統變數，代表該商品的排名（1 = 最高）

## 基本語法

```xs
// 主區塊
input: _Period(20, "均線週期");
var: _Score(0);

_Score = (Close - Average(Close, _Period)) / Average(Close, _Period) * 100;

if Volume > 500 then    // 基本篩選條件
    ret = _Score;        // 回傳排序值（越大排越前面）

// rank 區塊
rank:
    // 這裡無法使用 _Period 或 _Score
    if ranking <= 10 then  // 取前 10 名
        ret = 1;           // ret=1 表示選入
end;
```

## OutputField 輸出額外欄位

```xs
input: _Period(20, "週期");
var: _RSIValue(0);
var: _VolumeRatio(0);

_RSIValue = RSI(Close, _Period);
_VolumeRatio = Volume / Average(Volume, _Period);

OutputField("RSI值", _RSIValue);
OutputField("量比", _VolumeRatio);

if _RSIValue < 30 and _VolumeRatio > 2 then
    ret = _VolumeRatio;  // 用量比排序

rank:
    if ranking <= 20 then
        ret = 1;
end;
```

## 完整範例：外資買超 + 創新高選股

```xs
input: _Days(5, "連續天數");
input: _TopN(10, "選取檔數");
var: _BuySum(0);
var: _IsNewHigh(false);
var: _i(0);

// 計算 N 日外資累計買超
_BuySum = 0;
for _i = 0 to _Days - 1 begin
    _BuySum = _BuySum + GetField("外資買賣超(張)")[_i];
end;

// 判斷是否創 60 日新高
_IsNewHigh = High = Highest(High, 60);

OutputField("外資累買", _BuySum);
OutputField("創新高", _IsNewHigh);

if _BuySum > 0 and _IsNewHigh then
    ret = _BuySum;

rank:
    // 注意：這裡不能用 _TopN
    // 若需要動態數量，只能硬寫數字
    if ranking <= 10 then
        ret = 1;
end;
```

## 注意事項
- `ret` 在主區塊用於排序值，在 rank 區塊用於選入/排除（1=選入）
- 不設 `ret` 的商品會被自動排除
- `ranking` 只在 rank 區塊內有效
- rank 區塊的 `end;` 不能省略
