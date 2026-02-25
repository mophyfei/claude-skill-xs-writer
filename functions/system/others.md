# 日期/統計/量能/Array 函數 (24)

## 日期相關 (10)

| 函數 | 說明 | 語法 |
|------|------|------|
| `BarsLast(condition)` | 條件最後成立距今幾根 | `BarsLast(Close>Open)` |
| `DaysToExpiration` | 距到期日天數 | `DaysToExpiration` |
| `GetLastTradeDate` | 最後交易日期 | `GetLastTradeDate` |
| `LastDayOfMonth(date)` | 該月最後一天 | `LastDayOfMonth(20240301)` → 20240331 |
| `BarsSinceEntry` | 進場後經過K棒數 | `BarsSinceEntry` |
| `BarsSinceExit` | 出場後經過K棒數 | `BarsSinceExit` |

BarsLast 回傳整數。若條件從未成立，回傳 -1。

## 統計函數 (6)

| 函數 | 說明 | 語法 |
|------|------|------|
| `StandardDev(data,period)` | 標準差 | `StandardDev(Close,20)` |
| `Correlation(data1,data2,period)` | 相關係數(-1~1) | `Correlation(Close,Volume,20)` |
| `Covariance(data1,data2,period)` | 共變異數 | `Covariance(Close,Volume,20)` |
| `RSquare(data,period)` | R平方(決定係數) | `RSquare(Close,20)` |
| `Variance(data,period)` | 變異數 | `Variance(Close,20)` |

## 量能函數 (4)

| 函數 | 說明 | 語法 |
|------|------|------|
| `DiffBidAskVolumeLxL` | 逐筆內外盤差 | `DiffBidAskVolumeLxL` |
| `DiffUpDownVolume` | 上漲下跌量差 | `DiffUpDownVolume` |
| `UpVolume(period)` | 上漲成交量 | `UpVolume(20)` |
| `DownVolume(period)` | 下跌成交量 | `DownVolume(20)` |

## Array 系列函數 (4)

| 函數 | 說明 | 語法 |
|------|------|------|
| `ArraySeries(arr,size,data)` | 填入序列資料 | `ArraySeries(myArr,20,Close)` |
| `ArrayMASeries(arr,size,data,period)` | 填入均線序列 | `ArrayMASeries(myArr,20,Close,5)` |
| `ArrayLinearRegSlope(arr,size)` | 陣列線性回歸斜率 | `ArrayLinearRegSlope(myArr,20)` |
| `ArrayStandardDev(arr,size)` | 陣列標準差 | `ArrayStandardDev(myArr,20)` |

## 常用範例

```xs
// BarsLast：找上次金叉距今幾根
_BarsSinceGC = BarsLast(CrossOver(Average(Close,5), Average(Close,20)));

// 布林通道（用標準差）
_MA = Average(Close, 20);
_SD = StandardDev(Close, 20);
_Upper = _MA + 2 * _SD;
_Lower = _MA - 2 * _SD;

// 兩檔股票相關性
_Corr = Correlation(Close, GetSymbolField("2330","收盤價","D"), 60);

// 月底判斷
if Date = LastDayOfMonth(Date) then
    Alert("本月最後交易日");

// 逐筆內外盤差
if DiffBidAskVolumeLxL > 0 then
    _NetBuy = true;  // 外盤大於內盤
```
