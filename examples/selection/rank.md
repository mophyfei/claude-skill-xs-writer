# 選股範例：Rank 排名語法

## Rank 基本用法

```xs
// Rank 語法：依指定欄位排序，選出前N名或後N名
// Rank(值, "排序方式")
// "D" = 由大到小 (Descending)
// "A" = 由小到大 (Ascending)
// 回傳值為排名序號（1=第一名）

// 成交量前20名
if Rank(Volume, "D") <= 20 then
  ret = 1;
```

## 漲幅排行

```xs
// 今日漲幅前30名
variable: _chgPct(0);

_chgPct = GetField("漲跌幅");

if Rank(_chgPct, "D") <= 30 then
  ret = 1;
```

## 外資買超排行

```xs
// 外資買超前50名
variable: _foreignNet(0);

_foreignNet = GetField("外資買賣超");

// 只看買超的（正數），然後取前50
if _foreignNet > 0
   AND Rank(_foreignNet, "D") <= 50
then ret = 1;
```

## 低本益比排行

```xs
// 本益比最低的前30名（排除負值和極端值）
variable: _pe(0);

_pe = GetField("本益比");

if _pe > 0 AND _pe < 100    // 排除異常值
   AND Rank(_pe, "A") <= 30  // 由小到大前30名
then ret = 1;
```

## 高殖利率排行

```xs
// 殖利率最高前20名
variable: _yield(0);

_yield = GetField("殖利率");

if _yield > 0
   AND Rank(_yield, "D") <= 20  // 殖利率由高到低前20
then ret = 1;
```

## 複合排名選股

```xs
// 多因子排名：結合漲幅+量能+法人
variable: _chgRank(0), _volRank(0), _foreignRank(0);
variable: _totalScore(0);

_chgRank = Rank(GetField("漲跌幅"), "D");
_volRank = Rank(Volume, "D");
_foreignRank = Rank(GetField("外資買賣超"), "D");

// 綜合排名分數（排名越小=分數越低=越好）
_totalScore = _chgRank + _volRank + _foreignRank;

// 綜合分數最低的前20名
if Rank(_totalScore, "A") <= 20 then
  ret = 1;
```

## 營收成長排名

```xs
// 月營收年增率排名前30
variable: _revGrowth(0);

_revGrowth = GetField("月營收年增率");

if _revGrowth > 0                     // 只看正成長
   AND Rank(_revGrowth, "D") <= 30    // 成長率前30名
then ret = 1;
```

## 週轉率排名（活躍股）

```xs
// 週轉率最高的前50名（活躍股篩選）
variable: _turnover(0);

_turnover = GetField("週轉率");

if _turnover > 0
   AND Rank(_turnover, "D") <= 50
   AND Close > 10                // 排除低價股
   AND Volume > 500              // 基本量門檻
then ret = 1;
```

## ROE 排名 + 估值過濾

```xs
// ROE前20% + 本益比合理
variable: _roe(0), _pe(0);

_roe = GetField("股東權益報酬率");
_pe = GetField("本益比");

if _roe > 0 AND Rank(_roe, "D") <= 50  // ROE前50名
   AND _pe > 0 AND _pe < 20             // 本益比合理
then ret = 1;
```
