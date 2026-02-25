# 一般函數 (47)

## K 棒資訊

| 函數 | 說明 | 語法 |
|------|------|------|
| `BarAdjusted` | K 棒是否經過還原 | `if BarAdjusted then ...` |
| `BarFreq` | 目前 K 棒頻率 | `BarFreq` → "D","W","M","5" |
| `BarInterval` | K 棒間隔值 | `BarInterval` → 5 (5分K) |
| `CurrentBar` | 目前 K 棒編號 | `if CurrentBar = 1 then ...` |
| `SetBarFreq("freq")` | 設定 K 棒頻率 | `SetBarFreq("W")` |

## OutputField（選股腳本用）

| 函數 | 說明 | 語法 |
|------|------|------|
| `OutputField(val,"name")` | 輸出自訂欄位 | `OutputField(Close,"收盤")` |
| `OutputField1~8(val,"name")` | 輸出欄位 1~8 | `OutputField1(val,"漲幅")` |
| `SetOutputFieldTextColor(n,color)` | 設定欄位文字顏色 | `SetOutputFieldTextColor(1,"red")` |
| `SetOutputFieldColor(n,color)` | 設定欄位背景色 | `SetOutputFieldColor(1,"yellow")` |

```xs
// OutputField 範例（選股腳本）
OutputField1(Close, "收盤價");
OutputField2(Volume, "成交量");
if Close > Close[1] then
    SetOutputFieldTextColor(1, "red");
```

## Plot（指標腳本用）

| 函數 | 說明 | 語法 |
|------|------|------|
| `Plot(val,"name")` | 繪製數值線 | `Plot(Close,"收盤")` |
| `Plot1~8(val,"name")` | 繪製線 1~8 | `Plot1(MA5,"MA5")` |
| `Plot1~8(val,"name",chk)` | 帶 checkbox | `Plot2(MA20,"MA20",true)` |
| `PlotK(o,h,l,c)` | 繪製 K 棒 | `PlotK(Open,High,Low,Close)` |
| `SetPlotColor(n,color)` | 設定線顏色 | `SetPlotColor(1,"red")` |
| `SetPlotWidth(n,width)` | 設定線寬度 | `SetPlotWidth(1,2)` |
| `SetPlotStyle(n,style)` | 設定線樣式 | `SetPlotStyle(1,1)` |

```xs
// Plot 範例（指標腳本）
value1 = Average(Close, 5);
value2 = Average(Close, 20);
Plot1(value1, "MA5");
Plot2(value2, "MA20", true);
if value1 > value2 then
    SetPlotColor(1, "red")
else
    SetPlotColor(1, "green");
```

## 其他

| 函數 | 說明 | 語法 |
|------|------|------|
| `RaiseRunTimeError("msg")` | 拋出執行錯誤 | `RaiseRunTimeError("參數錯誤")` |
| `Commentary("text")` | 加入文字說明 | `Commentary("多頭信號")` |
| `Print(val)` | 除錯輸出 | `Print(Close)` |
| `MaxBarsBack` | 最大回溯期數 | `if CurrentBar > MaxBarsBack then ...` |
| `StatusLine(text)` | 狀態列顯示 | `StatusLine("計算中...")` |
| `SetBarsRequired(n)` | 設定所需K棒數 | `SetBarsRequired(100)` |

PlotStyle 值：0=實線, 1=虛線, 2=點線, 3=柱狀, 4=十字, 5=圓點
