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
variable: chgPct(0);

chgPct = GetField("漲幅(%)");

if Rank(chgPct, "D") <= 30 then
  ret = 1;
```

## 外資買超排行

```xs
// 外資買超前50名
variable: foreignNet(0);

foreignNet = GetField("外資買賣超");

// 只看買超的（正數），然後取前50
if foreignNet > 0
   AND Rank(foreignNet, "D") <= 50
then ret = 1;
```

## 低本益比排行

```xs
// 本益比最低的前30名（排除負值和極端值）
variable: pe(0);

pe = GetField("本益比");

if pe > 0 AND pe < 100    // 排除異常值
   AND Rank(pe, "A") <= 30  // 由小到大前30名
then ret = 1;
```

## 高殖利率排行

```xs
// 殖利率最高前20名
variable: yield(0);

yield = GetField("殖利率");

if yield > 0
   AND Rank(yield, "D") <= 20  // 殖利率由高到低前20
then ret = 1;
```

## 複合排名選股

```xs
// 多因子排名：結合漲幅+量能+法人
variable: chgRank(0), volRank(0), foreignRank(0);
variable: totalScore(0);

chgRank = Rank(GetField("漲幅(%)"), "D");
volRank = Rank(Volume, "D");
foreignRank = Rank(GetField("外資買賣超"), "D");

// 綜合排名分數（排名越小=分數越低=越好）
totalScore = chgRank + volRank + foreignRank;

// 綜合分數最低的前20名
if Rank(totalScore, "A") <= 20 then
  ret = 1;
```

## 營收成長排名

```xs
// 月營收年增率排名前30
// 注意：欄位名含單位後綴 (%)
variable: revGrowth(0);

revGrowth = GetField("月營收年增率(%)");

if revGrowth > 0                     // 只看正成長
   AND Rank(revGrowth, "D") <= 30    // 成長率前30名
then ret = 1;
```

## 週轉率排名（活躍股）

```xs
// 週轉率最高的前50名（活躍股篩選）
variable: turnover(0);

turnover = GetField("週轉率");

if turnover > 0
   AND Rank(turnover, "D") <= 50
   AND Close > 10                // 排除低價股
   AND Volume > 500              // 基本量門檻
then ret = 1;
```

## ROE 排名 + 估值過濾

```xs
// ROE前20% + 本益比合理
// 注意：ROE欄位含 (%) 後綴
variable: roe(0), pe(0);

roe = GetField("ROE(%)");
pe = GetField("本益比");

if roe > 0 AND Rank(roe, "D") <= 50  // ROE前50名
   AND pe > 0 AND pe < 20             // 本益比合理
then ret = 1;
```
