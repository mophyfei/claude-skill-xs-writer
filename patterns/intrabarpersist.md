# Intrabar Persistence 模式

## 背景
XQ 日內回測啟用逐筆撮合時，每個 tick 都會重新執行腳本。
一般 `var` 變數在每次 tick 執行時會**重新計算**，無法保留上一次的值。

## 何時需要 intrabarpersist
- **狀態追蹤**：記錄是否已觸發訊號
- **累計值**：累加成交量、計算 VWAP
- **趨勢方向**：記住當前多空狀態
- **移動停損**：追蹤最高/最低價

## 何時不需要
- 純計算變數（每次都會重新計算的值）
- 使用內建函數的結果（如 `Average`, `Highest`）
- 只在 K 棒完成時使用的值

## 語法

```xs
var intrabarpersist: _Flag(0);
var intrabarpersist: _TrailStop(0);
var intrabarpersist: _DayVolume(0);
```

## 範例：日內累計成交量

```xs
input: _Threshold(10000, "量能門檻");
var intrabarpersist: _CumVol(0);
var intrabarpersist: _Triggered(false);

// 換日重置
if date <> date[1] then begin
    _CumVol = 0;
    _Triggered = false;
end;

_CumVol = _CumVol + Volume;

if _CumVol >= _Threshold and _Triggered = false then begin
    _Triggered = true;
    plot1(Close, "突破量");
end;
```

## 範例：移動停損追蹤

```xs
var intrabarpersist: _TrailHigh(0);
var intrabarpersist: _InPosition(false);

if position > 0 and _InPosition = false then begin
    _InPosition = true;
    _TrailHigh = Close;
end;

if _InPosition then begin
    if High > _TrailHigh then
        _TrailHigh = High;

    if Close < _TrailHigh * 0.95 then begin
        setposition(0);
        _InPosition = false;
    end;
end;
```

## 注意事項
- `intrabarpersist` 宣告在 `var` 之後、變數名稱之前
- 換日時記得手動重置（用 `date <> date[1]`）
- 日 K 以上頻率不需要 intrabarpersist（每根 K 棒只執行一次）
