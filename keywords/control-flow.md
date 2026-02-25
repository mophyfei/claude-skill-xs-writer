# XS 流程控制關鍵字

## if / then / else

### 單行寫法
```xs
if Close > Open then _Signal = 1;
if Close > Open then _Signal = 1 else _Signal = -1;
```

### 多行寫法（begin/end 區塊）
```xs
if Close > Open then begin
    _Signal = 1;
    _Count = _Count + 1;
end;

if Close > Open then begin
    _Signal = 1;
end else begin
    _Signal = -1;
end;
```

### 巢狀 if
```xs
if Close > Open then begin
    if Volume > 1000 then
        _Signal = 2
    else
        _Signal = 1;
end else begin
    _Signal = 0;
end;
```

**注意**：`else` 前面的語句**不加分號**。

## for / to / begin / end

```xs
var: _Sum(0);
var: _i(0);

_Sum = 0;
for _i = 0 to 9 begin
    _Sum = _Sum + Close[_i];
end;
```

- 索引從 0 開始
- `to` 包含終止值（0 to 9 = 共 10 次）
- 迴圈體必須用 `begin/end` 包裹

### 巢狀迴圈
```xs
var: _i(0);
var: _j(0);
var: _Max(0);

_Max = 0;
for _i = 0 to 4 begin
    for _j = 0 to 4 begin
        if High[_i * 5 + _j] > _Max then
            _Max = High[_i * 5 + _j];
    end;
end;
```

## while / begin / end

```xs
var: _Count(0);

_Count = 0;
while Close[_Count] > Average(Close, 20)[_Count] and _Count < 100 begin
    _Count = _Count + 1;
end;
// _Count = 連續站上均線的天數
```

**注意**：務必設定上限防止無限迴圈（如 `_Count < 100`）。

## break

在迴圈中提前跳出：

```xs
var: _i(0);
var: _Found(false);

_Found = false;
for _i = 0 to 59 begin
    if Low[_i] < _SupportLevel then begin
        _Found = true;
        break;
    end;
end;
```

## return（一般腳本提前結束）

```xs
// 若不符合基本條件，直接結束腳本
if Volume = 0 then return;

// 後續邏輯只在有成交量時執行
_MA = Average(Close, 20);
plot1(_MA, "均線");
```

## ret（選股腳本回傳值）

```xs
// ret 在選股腳本中用於回傳排序值
if _Condition then
    ret = _Score;

// rank 區塊中 ret=1 表示選入
rank:
    if ranking <= 10 then ret = 1;
end;
```

**`return` 和 `ret` 是不同的東西**：
- `return`：結束腳本執行
- `ret`：設定選股回傳值
