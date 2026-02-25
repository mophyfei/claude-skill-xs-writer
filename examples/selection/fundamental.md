# 選股範例：基本面

> **重要：財務欄位名稱必須包含單位後綴如 (%)、(元)、(億)！**

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
// 注意：欄位名含單位後綴 (%)、(元)
if GetField("ROE(%)") > 15
   AND GetField("近四季每股盈餘(元)") > 3
   AND GetField("EPS年增率(%)") > 20
   AND GetField("毛利率(%)") > 30
then ret = 1;
```

## 營收成長動能

```xs
// 月營收連續成長
// 注意：欄位名含 (%) 和 (億) 後綴
if GetField("月營收年增率(%)") > 20
   AND GetField("月營收月增率(%)") > 5
   AND GetField("累計營收年增率(%)") > 15
   AND GetField("月營收(億)") > 1
then ret = 1;
```

## 財務穩健 + 獲利

```xs
// 低負債 + 高現金流 + 穩定獲利
// 注意：每個欄位的單位後綴都要正確
if GetField("負債比率(%)") < 40
   AND GetField("流動比率(%)") > 200
   AND GetField("自由現金流量(億)") > 0
   AND GetField("ROE(%)") > 12
   AND GetField("營業利益率(%)") > 10
then ret = 1;
```

## 現金流量選股

```xs
// 自由現金流充沛 + 獲利品質佳
if GetField("自由現金流量(億)") > 0
   AND GetField("營業現金流量佔營收比(%)") > 15
   AND GetField("每股自由現金流(元)") > 2
   AND GetField("近四季每股盈餘(元)") > 0
then ret = 1;
```

## 高殖利率 + 連續配息

```xs
// 穩定配息的存股標的
if GetField("殖利率") > 5
   AND GetField("連續配息年數") > 10
   AND GetField("股利發放率") > 50
   AND GetField("股利發放率") < 90   // 非過度配息
   AND GetField("ROE(%)") > 10
then ret = 1;
```

## 巴菲特式選股

```xs
// 護城河 + 穩定獲利 + 合理估值
if GetField("ROE(%)") > 15                    // 高ROE
   AND GetField("毛利率(%)") > 40              // 高毛利=護城河
   AND GetField("負債比率(%)") < 50            // 低負債
   AND GetField("近四季每股盈餘(元)") > 0       // 有獲利
   AND GetField("本益比") < 20                  // 估值合理
   AND GetField("營業現金流量佔營收比(%)") > 15 // 現金流佳
then ret = 1;
```

## 營收轉機股

```xs
// 營收由負轉正的轉機股
if GetField("月營收年增率(%)") > 10
   AND GetField("月營收年增率(%)")[1] < 0   // 上月還是負成長
   AND GetField("月營收月增率(%)") > 10      // 月增率也向上
   AND GetField("本益比") < 20               // 估值不過高
then ret = 1;
```
