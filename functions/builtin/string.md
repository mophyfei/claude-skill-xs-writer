# 字串函數 (15)

## 搜尋與擷取

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `InStr(str, sub)` | 搜尋子字串位置(1起) | `InStr("ABCDE","CD")` | 3 |
| `LeftStr(str, n)` | 取左邊 n 字元 | `LeftStr("Hello",3)` | "Hel" |
| `RightStr(str, n)` | 取右邊 n 字元 | `RightStr("Hello",3)` | "llo" |
| `MidStr(str, start, n)` | 取中間字元 | `MidStr("Hello",2,3)` | "ell" |
| `StrLen(str)` | 字串長度 | `StrLen("Hello")` | 5 |

## 轉換

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `NumToStr(num, dec)` | 數字轉字串 | `NumToStr(3.14, 2)` | "3.14" |
| `StrToNum(str)` | 字串轉數字 | `StrToNum("123")` | 123 |
| `Text(num, "fmt")` | 格式化數字 | `Text(1234,"#,##0")` | "1,234" |
| `UpperStr(str)` | 轉大寫 | `UpperStr("abc")` | "ABC" |
| `LowerStr(str)` | 轉小寫 | `LowerStr("ABC")` | "abc" |

## 修改

| 函數 | 說明 | 範例 | 結果 |
|------|------|------|------|
| `TrimStr(str)` | 去頭尾空白 | `TrimStr(" AB ")` | "AB" |
| `ReplaceStr(str,old,new)` | 取代子字串 | `ReplaceStr("AB","A","X")` | "XB" |
| `Spaces(n)` | 產生 n 個空格 | `Spaces(5)` | "     " |

## 常用範例

```xs
// 組合商品代碼與文字
_Msg = Symbol + " 收盤價: " + NumToStr(Close, 2);
Alert(_Msg);

// 判斷商品代碼前綴
if LeftStr(Symbol, 2) = "23" then
    Print("電子股");

// 格式化百分比
_PctStr = NumToStr((_Change / Close[1]) * 100, 2) + "%";

// 文字搜尋
if InStr(SymbolName, "ETF") > 0 then
    Print("此為 ETF");

// Text 格式化
_Display = Text(Volume, "#,##0");
```
