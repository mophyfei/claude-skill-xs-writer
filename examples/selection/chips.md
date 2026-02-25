# 選股範例：籌碼面 (僅台股)

## 三大法人同步買超

```xs
// 外資+投信+自營商同步買超
variable: foreign(0), trust(0), dealer(0);

foreign = GetField("外資買賣超");
trust = GetField("投信買賣超");
dealer = GetField("自營商買賣超");

if foreign > 0 AND trust > 0 AND dealer > 0
   AND (foreign + trust + dealer) > 500  // 合計買超500張以上
then ret = 1;
```

## 外資連續買超

```xs
// 外資連續N日買超
input: days(5, "連續天數");
variable: i(0), allBuy(true);

allBuy = true;
for i = 0 to days - 1 begin
  if GetField("外資買賣超")[i] <= 0 then
    allBuy = false;
end;

if allBuy
   AND GetField("外資持股比率") > 5  // 外資有一定持股
then ret = 1;
```

## 投信認養股

```xs
// 投信連續買超 + 持股比率增加
variable: trust5(0);

// 近5日投信買超合計
trust5 = GetField("投信買賣超")
       + GetField("投信買賣超")[1]
       + GetField("投信買賣超")[2]
       + GetField("投信買賣超")[3]
       + GetField("投信買賣超")[4];

if trust5 > 500                          // 5日合計買超500張
   AND GetField("投信持股比率") > 1       // 持股比>1%
   AND GetField("投信買賣超") > 0         // 今日仍在買
then ret = 1;
```

## 主力買超 + 集中度高

```xs
// 主力積極佈局
if GetField("主力買賣超") > 500          // 主力買超
   AND GetField("主力集中度") > 50        // 集中度高
   AND GetField("主力買進家數") > GetField("主力賣出家數")  // 買>賣
then ret = 1;
```

## 融券增加 = 潛在軋空

```xs
// 融券水位高 + 股價轉強 = 軋空
if GetField("券資比") > 20               // 券資比高
   AND GetField("融券增減") > 100         // 融券持續增加
   AND Close > Average(Close, 5)          // 股價在短均之上
   AND GetField("漲幅(%)") > 0           // 今日上漲
then ret = 1;
```

## 大戶持股增加

```xs
// 集保大戶增持 + 散戶減少
if GetField("千張以上持股比率") > GetField("千張以上持股比率")[1]
   AND GetField("集保戶數增減") < 0       // 戶數減少(籌碼集中)
   AND GetField("千張以上持股比率") > 50   // 大戶持股過半
then ret = 1;
```

## 法人+主力同步

```xs
// 法人與主力同步買超（強勢籌碼）
if GetField("外資買賣超") > 200
   AND GetField("投信買賣超") > 50
   AND GetField("主力買賣超") > 300
   AND Volume > Average(Volume, 20)       // 有量配合
   AND Close > Open                        // 收紅
then ret = 1;
```

## 融資減 + 法人買 = 籌碼沉澱

```xs
// 散戶退場+法人進場
if GetField("融資增減") < -100            // 融資大減
   AND GetField("外資買賣超") > 0          // 外資買
   AND GetField("投信買賣超") > 0          // 投信買
   AND GetField("借券餘額") < GetField("借券餘額")[5]  // 借券減
then ret = 1;
```

## 董監持股穩定 + 不質押

```xs
// 公司派對自家股票有信心
if GetField("董監持股比率") > 20          // 董監持股高
   AND GetField("董監質押比率") < 10       // 質押比低
   AND GetField("千張以上持股比率") > 40   // 大戶穩定持有
then ret = 1;
```
