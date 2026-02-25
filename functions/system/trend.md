# 趨勢分析 (12)

## 波段高低點

| 函數 | 說明 | 語法 |
|------|------|------|
| `SwingHigh(str,data,left,right)` | 波段高點 | `SwingHigh(1,High,3,3)` |
| `SwingLow(str,data,left,right)` | 波段低點 | `SwingLow(1,Low,3,3)` |

參數說明：
- `str`：強度(通常用1)
- `data`：資料來源
- `left`：左邊需高/低於幾根
- `right`：右邊需高/低於幾根

回傳值：若有找到回傳該點價格，否則回傳 -1。

## 線性回歸

| 函數 | 說明 | 語法 |
|------|------|------|
| `LinearReg(data,period)` | 線性回歸值 | `LinearReg(Close,20)` |
| `LinearRegSlope(data,period)` | 線性回歸斜率 | `LinearRegSlope(Close,20)` |
| `LinearRegAngle(data,period)` | 線性回歸角度 | `LinearRegAngle(Close,20)` |
| `Angle(data,period)` | 趨勢角度 | `Angle(Close,20)` |

## 趨勢判斷

| 函數 | 說明 | 語法 |
|------|------|------|
| `UpTrend(data)` | 上升趨勢判斷 | `UpTrend(Close)` |
| `DownTrend(data)` | 下降趨勢判斷 | `DownTrend(Close)` |

UpTrend/DownTrend 回傳 true/false。

## 常用範例

```xs
// 波段高低點偵測
_SH = SwingHigh(1, High, 5, 5);
_SL = SwingLow(1, Low, 5, 5);
if _SH <> -1 then
    Plot1(_SH, "波段高");
if _SL <> -1 then
    Plot2(_SL, "波段低");

// 線性回歸通道
_RegVal = LinearReg(Close, 20);
_Slope = LinearRegSlope(Close, 20);
Plot1(_RegVal, "回歸線");

// 斜率判斷趨勢方向
if _Slope > 0 then
    _Trend = 1    // 上升
else if _Slope < 0 then
    _Trend = -1;  // 下降

// 上升趨勢 + 回調買入
if UpTrend(Close) and Close < Average(Close, 5) then
    SetPosition(1000);

// 波段高低點連線斜率
if _SH <> -1 and _SH[1] <> -1 then begin
    if _SH > _SH[1] then
        _HigherHigh = true;
end;

// 角度過陡（超漲）
if Angle(Close, 10) > 60 then
    Alert("角度過陡，注意回檔");
```
