# 跨頻率函數 (32)

## xf_ 系列（跨大頻率）

用於在低頻率K棒（如日線）中取得高頻率（如週/月）資料。

| 函數 | 說明 | 語法 |
|------|------|------|
| `xf_GetValue("freq",data)` | 取跨頻率原始值 | `xf_GetValue("W",Close)` |
| `xf_Average("freq",data,period)` | 跨頻率均線 | `xf_Average("W",Close,20)` |
| `xf_EMA("freq",data,period)` | 跨頻率 EMA | `xf_EMA("M",Close,12)` |
| `xf_MACD("freq",data,fast,slow)` | 跨頻率 MACD | `xf_MACD("W",Close,12,26)` |
| `xf_MACDDiff("freq",data,fast,slow)` | 跨頻率 MACD 柱 | `xf_MACDDiff("W",Close,12,26)` |
| `xf_RSI("freq",data,period)` | 跨頻率 RSI | `xf_RSI("W",Close,14)` |
| `xf_Highest("freq",data,period)` | 跨頻率最高值 | `xf_Highest("W",High,20)` |
| `xf_Lowest("freq",data,period)` | 跨頻率最低值 | `xf_Lowest("W",Low,20)` |
| `xf_Stochastic("freq",period)` | 跨頻率 KD-K | `xf_Stochastic("W",9)` |
| `xf_StochasticD("freq",p,K,D)` | 跨頻率 KD-D | `xf_StochasticD("W",9,3,3)` |
| `xf_ATR("freq",period)` | 跨頻率 ATR | `xf_ATR("W",14)` |
| `xf_ADX("freq",period)` | 跨頻率 ADX | `xf_ADX("W",14)` |

頻率代碼：`"W"`=週, `"M"`=月, `"Q"`=季, `"Y"`=年

## xfMin_ 系列（跨分鐘頻率）

用於在分鐘K棒中取得不同分鐘頻率資料。

| 函數 | 說明 | 語法 |
|------|------|------|
| `xfMin_GetValue("freq",data)` | 取分鐘頻率值 | `xfMin_GetValue("30",Close)` |
| `xfMin_Average("freq",data,period)` | 分鐘頻率均線 | `xfMin_Average("60",Close,20)` |
| `xfMin_EMA("freq",data,period)` | 分鐘頻率 EMA | `xfMin_EMA("30",Close,12)` |
| `xfMin_MACD("freq",data,fast,slow)` | 分鐘頻率 MACD | `xfMin_MACD("60",Close,12,26)` |
| `xfMin_RSI("freq",data,period)` | 分鐘頻率 RSI | `xfMin_RSI("30",Close,14)` |
| `xfMin_Highest("freq",data,period)` | 分鐘頻率最高 | `xfMin_Highest("60",High,20)` |
| `xfMin_Lowest("freq",data,period)` | 分鐘頻率最低 | `xfMin_Lowest("60",Low,20)` |

分鐘頻率代碼：`"5"`, `"10"`, `"15"`, `"30"`, `"60"`

## 常用範例

```xs
// 日線中取週線均線
_WeekMA = xf_Average("W", Close, 20);
Plot1(_WeekMA, "週MA20");

// 5分K中取60分K的RSI
_RSI60 = xfMin_RSI("60", Close, 14);
if _RSI60 < 30 then Alert("60分RSI超賣");

// 多頻率共振：日線+週線同步金叉
_DayMACD = MACD(Close, 12, 26);
_WeekMACD = xf_MACD("W", Close, 12, 26);
if _DayMACD > 0 and _WeekMACD > 0 then
    _BullConfirm = true;
```
