# 價格計算 (13)

## 移動平均

| 函數 | 說明 | 語法 |
|------|------|------|
| `Average(data,period)` | 簡單移動平均(SMA) | `Average(Close,20)` |
| `EMA(data,period)` | 指數移動平均 | `EMA(Close,20)` |
| `XAverage(data,period)` | 同 EMA | `XAverage(Close,20)` |
| `WMA(data,period)` | 加權移動平均 | `WMA(Close,20)` |

EMA 與 XAverage 完全相同，可互換使用。

## 變化率

| 函數 | 說明 | 語法 |
|------|------|------|
| `RateOfChange(data,period)` | N期變化率 | `RateOfChange(Close,12)` |

公式：`(data - data[period]) / data[period] * 100`

## 區間計算

| 函數 | 說明 | 語法/公式 |
|------|------|---------|
| `Range` | 當根振幅 | `High - Low` |
| `TrueRange` | 真實區間 | `Max(H-L, |H-C[1]|, |L-C[1]|)` |
| `Summation(data,period)` | N期加總 | `Summation(Volume,20)` |
| `MidPoint(data,period)` | N期中點 | `(Highest+Lowest)/2` |

## 常用範例

```xs
// 均線系統
_MA5 = Average(Close, 5);
_MA10 = Average(Close, 10);
_MA20 = Average(Close, 20);
_MA60 = Average(Close, 60);

// 多頭排列
if _MA5 > _MA10 and _MA10 > _MA20 and _MA20 > _MA60 then
    _BullAlign = true;

// EMA 交叉
_FastEMA = EMA(Close, 12);
_SlowEMA = EMA(Close, 26);
if CrossOver(_FastEMA, _SlowEMA) then
    SetPosition(1000);

// 成交量均量
_VolMA = Average(Volume, 20);
if Volume > _VolMA * 2 then
    Alert("爆量！成交量超過均量2倍");

// 區間中點（唐奇安通道中線）
_MidLine = MidPoint(Close, 20);
Plot1(_MidLine, "中線");

// 累計成交量
_TotalVol = Summation(Volume, 5);

// 真實波幅比率
_ATRatio = TrueRange / Close * 100;
```
