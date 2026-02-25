# 期權相關 (12)

## Black-Scholes Greeks

| 函數 | 說明 | 語法 |
|------|------|------|
| `BSDelta` | Delta：標的價格敏感度 | `BSDelta` |
| `BSGamma` | Gamma：Delta 變化率 | `BSGamma` |
| `BSTheta` | Theta：時間衰減 | `BSTheta` |
| `BSVega` | Vega：波動率敏感度 | `BSVega` |
| `BSRho` | Rho：利率敏感度 | `BSRho` |

以上函數不需參數，直接回傳當前期權合約的希臘值。

## 波動率

| 函數 | 說明 | 語法 |
|------|------|------|
| `IVolatility` | 隱含波動率(IV) | `IVolatility` |
| `HVolatility(period)` | 歷史波動率(HV) | `HVolatility(20)` |

## 期權資訊

| 函數 | 說明 | 語法 |
|------|------|------|
| `DaysToExpiration` | 距到期日天數 | `DaysToExpiration` |
| `TheoreticalValue` | BS理論價格 | `TheoreticalValue` |

## 常用範例

```xs
// 顯示 Greeks
Plot1(BSDelta, "Delta");
Plot2(BSGamma, "Gamma");
Plot3(BSTheta, "Theta");
Plot4(BSVega, "Vega");

// IV 與 HV 比較
_IV = IVolatility;
_HV = HVolatility(20);
Plot1(_IV, "IV");
Plot2(_HV, "HV20");
if _IV > _HV * 1.5 then
    Alert("IV 顯著偏高");

// 到期日前 5 天警示
if DaysToExpiration <= 5 then
    Alert("即將到期，剩餘 " + NumToStr(DaysToExpiration,0) + " 天");

// 理論價與市價偏差
_Diff = Close - TheoreticalValue;
Plot1(_Diff, "價差");
if AbsValue(_Diff) > Close * 0.05 then
    Alert("市價偏離理論價超過5%");

// Delta 中性篩選
if AbsValue(BSDelta) >= 0.4 and AbsValue(BSDelta) <= 0.6 then
    OutputField1(BSDelta, "Delta");
```

注意：Greeks 函數僅適用於期權商品，在股票/期貨上使用無意義。
