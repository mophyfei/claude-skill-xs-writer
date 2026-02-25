# GROUP / GetSymbolGroup 模式

## 用途
在腳本中存取**一組商品**的資料，進行跨商品統計或比較。

## group 宣告語法

```xs
group: _MyGroup("自選群組名稱");
```

## 核心函數

| 函數 | 說明 |
|------|------|
| `GetSymbolGroup(_MyGroup)` | 取得群組物件 |
| `GroupSize(群組)` | 群組中的商品數量 |
| `GetSymbolField("代碼","欄位")` | 取特定商品欄位值 |
| `CheckSymbolField("代碼","欄位")` | 檢查欄位是否有資料 |

## 基本迴圈模式

```xs
group: _Group("我的群組");
var: _Count(0);
var: _Total(0);
var: _i(0);
var: _Symbol("");
var: _Size(0);

_Size = GroupSize(GetSymbolGroup(_Group));
_Total = 0;
_Count = 0;

for _i = 0 to _Size - 1 begin
    _Symbol = GetSymbolList(GetSymbolGroup(_Group), _i);

    if CheckSymbolField(_Symbol, "收盤價", "D") then begin
        _Total = _Total + GetSymbolField(_Symbol, "收盤價", "D");
        _Count = _Count + 1;
    end;
end;
```

## 重要：CheckSymbolField 先檢查再取值

```xs
// 正確：先檢查再取值
if CheckSymbolField(_Symbol, "月營收(億)", "D") then
    value1 = GetSymbolField(_Symbol, "月營收(億)", "D");

// 錯誤：未檢查直接取值，可能得到無效值
value1 = GetSymbolField(_Symbol, "月營收(億)", "D");
```

## 完整範例：成分股營收加總

```xs
// 計算群組內所有成分股的月營收加總
group: _Components("成分股群組");
var: _TotalRevenue(0);
var: _ValidCount(0);
var: _i(0);
var: _Sym("");
var: _N(0);
var: _Rev(0);

_N = GroupSize(GetSymbolGroup(_Components));
_TotalRevenue = 0;
_ValidCount = 0;

for _i = 0 to _N - 1 begin
    _Sym = GetSymbolList(GetSymbolGroup(_Components), _i);

    if CheckSymbolField(_Sym, "月營收(億)", "D") then begin
        _Rev = GetSymbolField(_Sym, "月營收(億)", "D");
        _TotalRevenue = _TotalRevenue + _Rev;
        _ValidCount = _ValidCount + 1;
    end;
end;

if _ValidCount > 0 then begin
    plot1(_TotalRevenue, "營收加總");
    plot2(_TotalRevenue / _ValidCount, "平均營收");
end;
```

## 注意事項
- `group` 宣告的名稱必須對應 XQ 中已建立的自選群組
- 群組商品數量有上限，過多可能影響效能
- `GetSymbolList` 回傳的是商品代碼字串
- 跨商品取值都應先用 `CheckSymbolField` 確認資料存在
- for 迴圈索引從 0 開始到 `_Size - 1`
