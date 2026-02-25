# 時間函數 (13)

## 取得時間

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `CurrentTime` | 當前系統時間(HHMMSS) | `CurrentTime` | 133025 |
| `Time` | K棒時間(HHMMSS) | `Time` | 090500 |

## 時間分解

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `Hour(time)` | 取小時 | `Hour(133025)` | 13 |
| `Minute(time)` | 取分鐘 | `Minute(133025)` | 30 |
| `Second(time)` | 取秒 | `Second(133025)` | 25 |

## 時間組合與運算

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `TimeValue(h,m,s)` | 組合時間值 | `TimeValue(9,30,0)` | 93000 |
| `TimeDiff(t1,t2)` | 時間差(秒) | `TimeDiff(090000,093000)` | 1800 |
| `TimeAdd(time,secs)` | 時間加秒數 | `TimeAdd(090000,1800)` | 093000 |

## 交易時段

| 函數 | 說明 | 範例 |
|------|------|------|
| `SessionStartTime` | 交易開盤時間 | `SessionStartTime` → 90000 |
| `SessionEndTime` | 交易收盤時間 | `SessionEndTime` → 133000 |

## 常用範例

```xs
// 開盤後 30 分鐘內不交易
if TimeDiff(SessionStartTime, Time) < 1800 then
    _InOpenPeriod = true;

// 收盤前 5 分鐘強制平倉
_ExitTime = TimeAdd(SessionEndTime, -300);
if Time >= _ExitTime and Position <> 0 then
    SetPosition(0);

// 僅在特定時段交易
if Time >= 093000 and Time <= 123000 then begin
    // 交易邏輯
end;

// 判斷是否盤中（用分鐘K棒）
if Time >= SessionStartTime and Time <= SessionEndTime then
    _InSession = true;

// 計算距收盤剩餘秒數
_SecsLeft = TimeDiff(Time, SessionEndTime);
```

注意：時間格式為 HHMMSS 整數（如 90000 表示 09:00:00）。
