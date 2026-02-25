# 日期函數 (16)

## 取得日期

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `CurrentDate` | 當前系統日期 | `CurrentDate` | 20240315 |
| `Date` | K棒日期(YYYYMMDD) | `Date` | 20240315 |
| `CurrentMonth` | 當前月份 | `CurrentMonth` | 3 |
| `CurrentYear` | 當前年份 | `CurrentYear` | 2024 |

## 日期分解

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `Year(date)` | 取年份 | `Year(20240315)` | 2024 |
| `Month(date)` | 取月份 | `Month(20240315)` | 3 |
| `DayOfMonth(date)` | 取日 | `DayOfMonth(20240315)` | 15 |
| `DayOfWeek(date)` | 取星期幾 | `DayOfWeek(20240315)` | 5(五) |

DayOfWeek 值：0=日, 1=一, 2=二, 3=三, 4=四, 5=五, 6=六

## 日期運算

| 函數 | 說明 | 語法 |
|------|------|------|
| `DateAdd("unit", n, date)` | 日期加減 | `DateAdd("D", 5, 20240101)` |
| `DateDiff("unit", d1, d2)` | 日期差距 | `DateDiff("D", 20240101, 20240110)` → 9 |

DateAdd / DateDiff 單位：`"D"`=天, `"M"`=月, `"Y"`=年

## 日期轉換

| 函數 | 說明 | 語法 |
|------|------|------|
| `DateToJulian(date)` | YYYYMMDD → Julian日 | `DateToJulian(20240101)` |
| `JulianToDate(julian)` | Julian日 → YYYYMMDD | `JulianToDate(2460311)` |

## 常用範例

```xs
// 判斷月初第一根K棒
if Month(Date) <> Month(Date[1]) then
    Print("新月份開始");

// 計算距今天數
_DaysAgo = DateDiff("D", Date, CurrentDate);

// 僅週一進場
if DayOfWeek(Date) = 1 and Position = 0 then
    SetPosition(1000);

// 加 30 天
_FutureDate = DateAdd("D", 30, CurrentDate);

// 跨年判斷
if Year(Date) <> Year(Date[1]) then
    Print("新年度");
```
