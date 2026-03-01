# 選股範例：籌碼面 (僅台股)

## 三大法人同步買超

```xs
// 外資+投信+自營商同步買超
variable: _foreign(0), _trust(0), _dealer(0);

_foreign = GetField("外資買賣超");
_trust = GetField("投信買賣超");
_dealer = GetField("自營商買賣超");

if _foreign > 0 AND _trust > 0 AND _dealer > 0
   AND (_foreign + _trust + _dealer) > 500  // 合計買超500張以上
then ret = 1;
```

## 外資連續買超

```xs
// 外資連續N日買超
input: _days(5, "連續天數");
variable: _i(0), _allBuy(true);

_allBuy = true;
for _i = 0 to _days - 1 begin
  if GetField("外資買賣超")[_i] <= 0 then
    _allBuy = false;
end;

if _allBuy
   AND GetField("外資持股比例") > 5  // 外資有一定持股
then ret = 1;
```

## 投信認養股

```xs
// 投信連續買超 + 持股比例增加
variable: _trust5(0);

// 近5日投信買超合計
_trust5 = GetField("投信買賣超")
       + GetField("投信買賣超")[1]
       + GetField("投信買賣超")[2]
       + GetField("投信買賣超")[3]
       + GetField("投信買賣超")[4];

if _trust5 > 500                          // 5日合計買超500張
   AND GetField("投信持股比例") > 1       // 持股比>1%
   AND GetField("投信買賣超") > 0         // 今日仍在買
then ret = 1;
```

## 主力積極佈局

```xs
// 主力買超 + 買進金額大於賣出金額
if GetField("主力買賣超張數") > 500          // 主力買超
   AND GetField("主力買進金額") > GetField("主力賣出金額")  // 買>賣
then ret = 1;
```

## 融券增加 = 潛在軋空

```xs
// 融券水位高 + 股價轉強 = 軋空
if GetField("券資比") > 20                   // 券資比高
   AND GetField("融券增減張數") > 100         // 融券持續增加
   AND Close > Average(Close, 5)              // 股價在短均之上
   AND GetField("漲跌幅") > 0                // 今日上漲
then ret = 1;
```

## 大戶持股增加

```xs
// 集保大戶增持 + 散戶減少
// 注意：大戶/散戶持股需指定 param 級距
if GetField("大戶持股比例", param:=400) > GetField("大戶持股比例", param:=400)[1]
   AND GetField("散戶持股比例", param:=400) < GetField("散戶持股比例", param:=400)[1]
then ret = 1;
```

## 法人+主力同步

```xs
// 法人與主力同步買超（強勢籌碼）
if GetField("外資買賣超") > 200
   AND GetField("投信買賣超") > 50
   AND GetField("主力買賣超張數") > 300
   AND Volume > Average(Volume, 20)       // 有量配合
   AND Close > Open                        // 收紅
then ret = 1;
```

## 融資減 + 法人買 = 籌碼沉澱

```xs
// 散戶退場+法人進場
if GetField("融資增減張數") < -100            // 融資大減
   AND GetField("外資買賣超") > 0              // 外資買
   AND GetField("投信買賣超") > 0              // 投信買
   AND GetField("借券餘額張數") < GetField("借券餘額張數")[5]  // 借券減
then ret = 1;
```

## 董監持股穩定

```xs
// 公司派對自家股票有信心
if GetField("董監持股佔股本比例") > 20          // 董監持股高
   AND GetField("董監質設比例") < 10            // 質設比低
then ret = 1;
```
