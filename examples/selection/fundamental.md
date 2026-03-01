# 選股範例：基本面

> **重要：欄位名稱必須完全匹配 xs-helper 官方名稱，不可自創！**

## 價值型選股

```xs
// 低本益比 + 高殖利率 + 低股價淨值比
if GetField("本益比") > 0 AND GetField("本益比") < 12
   AND GetField("殖利率") > 6
   AND GetField("股價淨值比") < 1.5
then ret = 1;
```

## 高獲利成長股

```xs
// ROE高 + EPS成長 + 毛利率高
if GetField("股東權益報酬率") > 15
   AND GetField("每股稅後淨利(元)") > 3
   AND GetField("營業毛利率") > 30
then ret = 1;
```

## 營收成長動能

```xs
// 月營收連續成長
if GetField("月營收年增率") > 20
   AND GetField("月營收月增率") > 5
   AND GetField("累計營收年增率") > 15
then ret = 1;
```

## 財務穩健 + 獲利

```xs
// 低負債 + 高現金流 + 穩定獲利
if GetField("負債比率") < 40
   AND GetField("流動比率") > 200
   AND GetField("自由現金流量") > 0
   AND GetField("股東權益報酬率") > 12
   AND GetField("營業利益率") > 10
then ret = 1;
```

## 現金流量選股

```xs
// 現金流量充沛選股
if GetField("自由現金流量") > 0
   AND GetField("每股自由現金流量") > 2
   AND GetField("每股稅後淨利(元)") > 0
then ret = 1;
```

## 高殖利率選股

```xs
// 穩定配息的存股標的
if GetField("殖利率") > 5
   AND GetField("現金股利") > 0
   AND GetField("股東權益報酬率") > 10
then ret = 1;
```

## 巴菲特式選股

```xs
// 護城河 + 穩定獲利 + 合理估值
if GetField("股東權益報酬率") > 15           // 高ROE
   AND GetField("營業毛利率") > 40            // 高毛利=護城河
   AND GetField("負債比率") < 50              // 低負債
   AND GetField("每股稅後淨利(元)") > 0       // 有獲利
   AND GetField("本益比") < 20                // 估值合理
then ret = 1;
```

## 營收轉機股

```xs
// 營收由負轉正的轉機股
if GetField("月營收年增率") > 10
   AND GetField("月營收年增率")[1] < 0   // 上月還是負成長
   AND GetField("月營收月增率") > 10      // 月增率也向上
   AND GetField("本益比") < 20            // 估值不過高
then ret = 1;
```
