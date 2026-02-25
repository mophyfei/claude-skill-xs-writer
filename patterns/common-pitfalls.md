# 常見陷阱與錯誤表

## 1. AvgPrice 函數 vs GetField("AvgPrice")

```xs
// AvgPrice 函數：(O+H+L+C)/4 的簡單平均
value1 = AvgPrice;

// GetField("均價")：成交均價（成交金額/成交量），完全不同的值！
value2 = GetField("均價(元)");
```

**兩者數值差異很大，不要搞混。**

## 2. plot / PlotK 互斥

```xs
// 錯誤：同一腳本不能混用
plot1(_MA, "均線");
PlotK(1, Open, High, Low, Close, "K棒");  // 衝突！

// 正確：拆成兩個腳本
```

## 3. newday 不存在

```xs
// 錯誤：XS 沒有 newday 關鍵字
if newday then ...

// 正確
if date <> date[1] then ...
```

## 4. 跨頻率變數覆蓋

```xs
// 錯誤：在 5 分 K 中存日線資料到變數
var: _DClose(0);
_DClose = GetField("收盤價", "D");  // 每個 tick 都被覆蓋

// 正確：直接使用，不存變數
if Close > GetField("收盤價", "D") then ...
```

## 5. 商品支援靜默失敗

```xs
// 美股上取外資買超 → 回傳 0，不報錯
value1 = GetField("外資買賣超(張)");  // 美股上永遠 = 0

// 寫腳本前必須確認欄位與商品的相容性
```

## 6. 非 XS 語法

```xs
// 錯誤：這些不是 XS 函數
value1 = MINVAL(a, b);        // 不存在
value2 = MAXVAL(a, b);        // 不存在
if marketposition = 1 then ... // 不是 XS

// 正確替代
value1 = MinList(a, b);
value2 = MaxList(a, b);
if position = 1 then ...
```

## 7. InputKind 型別不匹配

```xs
// 錯誤：預設值 1（整數）但 Dict 用 1.0（浮點數）
input: _Type(1, "類型", InputKind:=Dict([1.0,"A",2.0,"B"]));

// 正確：型別一致
input: _Type(1, "類型", InputKind:=Dict([1,"A",2,"B"]));
```

## 8. 缺少 `_` 前綴

```xs
// 錯誤
input: Period(20, "週期");
var: Signal(0);

// 正確
input: _Period(20, "週期");
var: _Signal(0);
```

## 9. GetQuote 無歷史資料

```xs
// 錯誤：GetQuote 不能回溯
value1 = GetQuote("成交價")[1];  // 無效！

// GetQuote 只有當下即時值，用於警示/交易腳本
value1 = GetQuote("成交價");  // 只有當前值
```

## 10. 欄位名稱少了單位後綴

```xs
// 錯誤
GetField("外資買賣超")    // 少了(張)
GetField("殖利率")        // 少了(%)

// 正確
GetField("外資買賣超(張)")
GetField("殖利率(%)")
```

## 11. var 寫了說明文字

```xs
// 錯誤：var 不能寫說明
var: _Signal(0, "訊號變數");

// 正確：var 只有名稱和初始值
var: _Signal(0);
```

## 12. 比較用了 ==

```xs
// 錯誤：XS 沒有 ==
if _Signal == 1 then ...

// 正確：用 =
if _Signal = 1 then ...
```
