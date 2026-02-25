# 交易單位換算規則

## 核心規則
XQ **不支援零股交易**，台股最小交易單位為 **1000 股（1 張）**。

## 標準換算公式

```xs
input: _Amount(1000000, "投入金額");
var: _Price(0);
var: _Lots(0);
var: _Shares(0);

_Price = Close;
_Lots = IntPortion(_Amount / (_Price * 1000));
_Shares = _Lots * 1000;
```

## 禁止的寫法

```xs
// 錯誤：會算出零股數量
_Shares = IntPortion(_Amount / _Price);  // 禁止！

// 錯誤：可能產生非整張數
_Shares = _Amount / _Price;  // 禁止！
```

**為什麼錯？** `IntPortion(1000000 / 150)` = 6666 股 = 6.666 張，XQ 無法執行。

## 正確的完整交易範例

```xs
input: _Amount(500000, "投入金額");
input: _MAPeriod(20, "均線週期");
var: _Lots(0);
var: _Shares(0);
var: _MA(0);

_MA = Average(Close, _MAPeriod);

if position = 0 and Close cross over _MA then begin
    _Lots = IntPortion(_Amount / (Close * 1000));
    if _Lots >= 1 then begin
        _Shares = _Lots * 1000;
        setposition(1, _Shares);
    end;
end;

if position = 1 and Close cross under _MA then
    setposition(0);
```

## 加碼部位範例

```xs
input: _AddAmount(200000, "加碼金額");
var: _AddLots(0);
var: _AddShares(0);

// 加碼時也要換算成整張
if position > 0 and _AddCondition then begin
    _AddLots = IntPortion(_AddAmount / (Close * 1000));
    if _AddLots >= 1 then begin
        _AddShares = _AddLots * 1000;
        setposition(1, filled + _AddShares);
    end;
end;
```

## 注意事項
- 永遠用 `IntPortion` 無條件捨去小數（不是四捨五入）
- 先除以 `(價格 * 1000)` 得到張數，再乘回 1000 得到股數
- 計算後檢查 `_Lots >= 1`，避免金額不足時下 0 張的單
- 美股不適用此規則（美股以 1 股為單位）
