# XS 資料型別與宣告

## input：參數宣告

使用者可調整的參數，帶有預設值和說明文字。

```xs
// 基本語法：名稱(預設值, "說明")
input: _Period(20, "均線週期");
input: _Threshold(0.05, "門檻值");
input: _UseFiler(true, "啟用過濾");

// 帶 InputKind 下拉選單
input: _Type(1, "類型",
    InputKind:=Dict([1,"SMA",2,"EMA"]),
    Quickedit:=True);

// 字串參數
input: _FieldName("收盤價", "欄位名稱");
```

**規則**：名稱必須以 `_` 開頭，必須有說明文字。

## var：變數宣告

腳本內部使用的變數，只有名稱和初始值。

```xs
// 基本語法：名稱(初始值)
var: _Signal(0);
var: _Price(0.0);
var: _Flag(false);
var: _Name("");
var: _Count(0);

// 多個變數宣告
var: _High(0), _Low(0), _Mid(0);
```

**規則**：名稱以 `_` 開頭，**不寫說明文字**。

## intrabarpersist：逐筆持續變數

日內逐筆撮合時保持值不被重置。

```xs
var intrabarpersist: _CumVolume(0);
var intrabarpersist: _DayHigh(0);
var intrabarpersist: _Entered(false);
```

只在日內回測（tick-by-tick）時有意義，日 K 以上不需要。

## value1 ~ value99：內建數值變數

系統預設的數值型變數，不需宣告，可直接使用。

```xs
value1 = Average(Close, 20);
value2 = RSI(Close, 14);
value3 = value1 - value2;

plot1(value1, "MA20");
plot2(value2, "RSI");
```

適合簡單腳本或快速測試，正式腳本建議用 `var` 命名。

## condition1 ~ condition99：內建布林變數

系統預設的布林型變數，不需宣告。

```xs
condition1 = Close > Average(Close, 20);
condition2 = Volume > Average(Volume, 10) * 2;

if condition1 and condition2 then
    plot1(1, "訊號");
```

## 字串變數

```xs
var: _Msg("");
var: _Symbol("");

_Msg = "目前價格: " + NumToStr(Close, 2);
_Symbol = GetSymbolList(GetSymbolGroup(_Group), _i);
```

## 陣列宣告

```xs
// 固定大小陣列
array: _Prices[10](0);
array: _Names[5]("");

// 使用
_Prices[0] = Close;
_Prices[1] = Close[1];
```

**注意**：多週期資料判斷不要用陣列，直接用 `[n]` 索引。

## 型別總覽

| 宣告方式 | 用途 | 需要 `_` 前綴 | 需要說明 |
|----------|------|:---:|:---:|
| input | 使用者參數 | O | O |
| var | 內部變數 | O | X |
| intrabarpersist | 逐筆持續 | O | X |
| value1~99 | 快速數值 | X | X |
| condition1~99 | 快速布林 | X | X |
| array | 陣列 | O | X |
