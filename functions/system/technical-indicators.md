# 技術指標 (50)

## 趨勢指標

| 函數 | 說明 | 語法 |
|------|------|------|
| `MACD(data,fast,slow)` | MACD 線 | `MACD(Close,12,26)` |
| `MACDDiff(data,fast,slow)` | MACD 柱狀(OSC) | `MACDDiff(Close,12,26)` |
| `ADI` | 累計/分配指標 | `ADI` |
| `ADX(period)` | 平均趨向指標 | `ADX(14)` |
| `DMI_Plus(period)` | +DI 正向指標 | `DMI_Plus(14)` |
| `DMI_Minus(period)` | -DI 負向指標 | `DMI_Minus(14)` |
| `SAR(accel,max)` | 拋物線轉向 | `SAR(0.02,0.2)` |
| `ACC` | 加速度指標 | `ACC` |

## 動量指標

| 函數 | 說明 | 語法 |
|------|------|------|
| `RSI(data,period)` | 相對強弱指標 | `RSI(Close,14)` |
| `Stochastic(period)` | 隨機指標 K 值 | `Stochastic(9)` |
| `StochasticD(period,K,D)` | 隨機指標 D 值 | `StochasticD(9,3,3)` |
| `CCI(period)` | 順勢指標 | `CCI(14)` |
| `WilliamsR(period)` | 威廉指標 | `WilliamsR(14)` |
| `Momentum(data,period)` | 動量指標 | `Momentum(Close,12)` |
| `PSY(period)` | 心理線 | `PSY(12)` |
| `TRIX(period)` | 三重指數平滑 | `TRIX(12)` |

## 波動指標

| 函數 | 說明 | 語法 |
|------|------|------|
| `ATR(period)` | 平均真實區間 | `ATR(14)` |
| `BollingerBand(data,period,devs)` | 布林上軌 | `BollingerBand(Close,20,2)` |
| `BollingerBandBot(data,period,devs)` | 布林下軌 | `BollingerBandBot(Close,20,2)` |
| `BollingerBandWidth(data,period,up,down)` | 布林帶寬 | `BollingerBandWidth(Close,20,2,2)` |

## 成交量指標

| 函數 | 說明 | 語法 |
|------|------|------|
| `OBV` | 能量潮指標 | `OBV` |
| `VR(period)` | 成交量比率 | `VR(26)` |

## 乖離率

| 函數 | 說明 | 語法 |
|------|------|------|
| `BIAS(data,period)` | 乖離率 | `BIAS(Close,20)` |

## 常用範例

```xs
// KD 指標
_K = Stochastic(9);
_D = StochasticD(9, 3, 3);
if CrossOver(_K, _D) and _K < 20 then
    SetPosition(1000);

// MACD 金叉
if CrossOver(MACD(Close,12,26), 0) then
    Alert("MACD 翻多");

// 布林通道突破
_Upper = BollingerBand(Close, 20, 2);
_Lower = BollingerBandBot(Close, 20, 2);
if Close > _Upper then Alert("突破上軌");

// ATR 停損
_Stop = Close - 2 * ATR(14);

// DMI 趨勢判斷
if DMI_Plus(14) > DMI_Minus(14) and ADX(14) > 25 then
    _StrongUpTrend = true;
```
