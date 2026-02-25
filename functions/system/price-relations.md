# 價格關係 (25)

## 極值位置

| 函數 | 說明 | 語法 |
|------|------|------|
| `HighestBar(data,period)` | 最高值出現在幾根前 | `HighestBar(High,20)` |
| `LowestBar(data,period)` | 最低值出現在幾根前 | `LowestBar(Low,20)` |
| `NthHighest(n,data,period)` | 第 n 高值 | `NthHighest(2,High,20)` |
| `NthLowest(n,data,period)` | 第 n 低值 | `NthLowest(2,Low,20)` |

## 連續漲跌天數

| 函數 | 說明 | 語法 |
|------|------|------|
| `HighDays(data)` | data 連續上漲天數 | `HighDays(Close)` |
| `LowDays(data)` | data 連續下跌天數 | `LowDays(Close)` |

HighDays 回傳正整數表示連漲天數；LowDays 同理。

## 增減率（基本面常用）

| 函數 | 說明 | 語法 |
|------|------|------|
| `MoM(data)` | 月增率(%) | `MoM(GetField("營收","M"))` |
| `QoQ(data)` | 季增率(%) | `QoQ(GetField("EPS","Q"))` |
| `YoY(data)` | 年增率(%) | `YoY(GetField("營收","M"))` |
| `PercentChange(data,period)` | N 期變化率(%) | `PercentChange(Close,20)` |

## 價格比率

| 函數 | 說明 | 語法 |
|------|------|------|
| `PercentR(period)` | 百分比排名 | `PercentR(14)` |
| `TrueHigh` | 真實最高(含前收) | `TrueHigh` |
| `TrueLow` | 真實最低(含前收) | `TrueLow` |

## 常用範例

```xs
// 找出20日最高價出現在幾天前
_BarsAgo = HighestBar(High, 20);
_HighPrice = High[_BarsAgo];

// 判斷創新高後回檔
if HighestBar(High, 60) = 0 then
    _NewHigh = true;  // 今天就是60日最高

// 第2高值作為壓力
_Resistance = NthHighest(2, High, 20);

// 連漲超過5天
if HighDays(Close) >= 5 then
    Alert("連漲5天以上");

// 營收年增率選股
_YoYRev = YoY(GetField("營收", "M"));
if _YoYRev > 20 then
    OutputField1(_YoYRev, "營收YoY%");

// 20日漲幅超過10%
if PercentChange(Close, 20) > 10 then
    _StrongUp = true;

// 找波段底部
_BarsSinceLow = LowestBar(Low, 60);
if _BarsSinceLow >= 20 then
    _BottomForming = true;
```
