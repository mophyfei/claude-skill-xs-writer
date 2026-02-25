# InputKind 下拉選單模式

## 語法

```xs
input: _Variable(預設值, "說明", InputKind:=Dict([值1,"文字1",值2,"文字2",...]), Quickedit:=True);
```

## 核心規則
- 預設值**必須**與 Dict 中第一個參數的**值和型別**完全一致
- 整數預設值對應整數選項、浮點數預設值對應浮點數選項

## 型別匹配範例

### 整數型

```xs
// 正確：預設值 1 是整數，Dict 第一個值也是整數 1
input: _Direction(1, "方向",
    InputKind:=Dict([1,"做多",2,"做空",3,"多空皆可"]),
    Quickedit:=True);
```

### 浮點數型

```xs
// 正確：預設值 0.5 是浮點數，Dict 值也是浮點數
input: _Ratio(0.5, "比例",
    InputKind:=Dict([0.5,"50%",1.0,"100%",1.5,"150%"]),
    Quickedit:=True);
```

### 型別不匹配（錯誤）

```xs
// 錯誤：預設值 1 是整數，但 Dict 第一個值 1.0 是浮點數
input: _Type(1, "類型",
    InputKind:=Dict([1.0,"類型A",2.0,"類型B"]));

// 錯誤：預設值 2 不是 Dict 的第一個值
input: _Mode(2, "模式",
    InputKind:=Dict([1,"模式A",2,"模式B"]));
// 修正：預設值改為 1（Dict 第一個值）
input: _Mode(1, "模式",
    InputKind:=Dict([1,"模式A",2,"模式B"]));
```

## 完整範例：均線交叉策略

```xs
input: _MAType(1, "均線類型",
    InputKind:=Dict([1,"SMA 簡單均線",2,"EMA 指數均線",3,"WMA 加權均線"]),
    Quickedit:=True);
input: _Period(20, "均線週期");
var: _MA(0);

if _MAType = 1 then
    _MA = Average(Close, _Period)
else if _MAType = 2 then
    _MA = XAverage(Close, _Period)
else if _MAType = 3 then
    _MA = WAverage(Close, _Period);

plot1(_MA, "均線");
plot2(Close, "收盤價");
```

## 注意事項
- `Quickedit:=True` 可讓使用者在圖表上快速切換選項
- Dict 內的值不一定要連續（可以是 1, 5, 10 等）
- 文字部分會顯示在下拉選單中，供使用者選擇
- 不加 `InputKind` 時，input 預設為數字輸入框
