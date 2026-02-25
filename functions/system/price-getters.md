# 價格取得 (33)

## 區間極值

| 函數 | 說明 | 語法 |
|------|------|------|
| `Highest(data,period)` | N 期最高值 | `Highest(High,20)` |
| `Lowest(data,period)` | N 期最低值 | `Lowest(Low,20)` |

## 特殊價格

| 函數 | 說明 | 公式 |
|------|------|------|
| `AvgPrice` | 均價 | (O+H+L+C)/4 |
| `TypicalPrice` | 典型價格 | (H+L+C)/3 |
| `MedianPrice` | 中間價格 | (H+L)/2 |
| `WeightedClose` | 加權收盤 | (H+L+C+C)/4 |

## 日頻率價格（D 系列）

| 函數 | 說明 | 範例 |
|------|------|------|
| `CloseD(n)` | 前 n 日收盤價 | `CloseD(1)` = 昨收 |
| `OpenD(n)` | 前 n 日開盤價 | `OpenD(0)` = 今開 |
| `HighD(n)` | 前 n 日最高價 | `HighD(1)` = 昨高 |
| `LowD(n)` | 前 n 日最低價 | `LowD(1)` = 昨低 |
| `VolumeD(n)` | 前 n 日成交量 | `VolumeD(1)` = 昨量 |

n=0 表示當日, n=1 表示前一日, n=2 表示前兩日

## 週頻率價格（W 系列）

| 函數 | 說明 | 範例 |
|------|------|------|
| `CloseW(n)` | 前 n 週收盤價 | `CloseW(1)` = 上週收 |
| `OpenW(n)` | 前 n 週開盤價 | `OpenW(0)` = 本週開 |
| `HighW(n)` | 前 n 週最高價 | `HighW(1)` |
| `LowW(n)` | 前 n 週最低價 | `LowW(1)` |

## 月頻率價格（M 系列）

| 函數 | 說明 | 範例 |
|------|------|------|
| `CloseM(n)` | 前 n 月收盤價 | `CloseM(1)` = 上月收 |
| `OpenM(n)` | 前 n 月開盤價 | `OpenM(0)` |
| `HighM(n)` | 前 n 月最高價 | `HighM(1)` |
| `LowM(n)` | 前 n 月最低價 | `LowM(1)` |

## 常用範例

```xs
// 突破 20 日高點
if Close > Highest(High, 20) then
    Alert("突破20日新高");

// 跌破 10 日低點
if Close < Lowest(Low, 10) then
    Alert("跌破10日新低");

// 分鐘K棒取日頻率資料
_YesterdayClose = CloseD(1);
_TodayOpen = OpenD(0);
_Gap = _TodayOpen - _YesterdayClose;

// 週線支撐壓力
_WeekHigh = HighW(1);
_WeekLow = LowW(1);

// 通道突破
_Upper = Highest(High, 20);
_Lower = Lowest(Low, 20);
_Mid = (_Upper + _Lower) / 2;
```
