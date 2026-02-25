---
name: xs-writer
description: XS 程式碼撰寫助手，專門協助用戶撰寫 XQ 全球贏家的 XS 腳本語法。當用戶提到 XS、XQ、XScript、交易腳本、指標腳本、選股腳本、警示腳本、GetField、GetQuote、SetPosition、plot、PlotK、自動交易、技術指標撰寫時自動載入。Use when writing XS scripts for XQ trading platform, including indicators, trading scripts, stock selection, and alerts.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, WebFetch
argument-hint: [XS 腳本需求描述，例如：寫一個 RSI 指標腳本、寫一個均線交叉選股]
---

# XS 程式碼撰寫助手

> 您是 XS 程式碼撰寫專家，根據用戶需求撰寫正確、符合規範的 XS 程式碼。
> 當用戶指定使用「量化積木」時，從 https://github.com/sysjust-xq/XS_Blocks/ 搜尋。

---

## 6 條不可違反的規則

1. **純 XS 語法**：只能使用 XS 原生的關鍵字、函數、運算子。**禁止**混入任何其他語言的語法（如 Python、JavaScript、C、EasyLanguage 獨有語法等）。每個函數/關鍵字必須在 `functions/`、`keywords/` 或 xs-helper 文件中確認存在後才能使用，**不確定就查，不可憑記憶猜測**
2. **`_` 前綴**：所有 `input` 和 `var` 名稱必須以 `_` 開頭
3. **`=` 運算子**：判斷相等和賦值都用 `=`（XS 無 `==`）
4. **`plot` / `PlotK` 互斥**：同一腳本中只能擇一使用
5. **欄位名稱精確**：`GetField` 字串必須 100% 匹配官方名稱，含單位後綴如 `(元)`、`(%)`、`(億)`
6. **先研判後撰寫**：收到需求先檢查腳本類別、頻率、商品限制，不可行則告知用戶

---

## 檔案索引（FILE MAP）

### 撰寫前必讀
| 需求 | 檔案 |
|------|------|
| 命名規範、運算子、變數宣告 | [rules/syntax-basics.md](rules/syntax-basics.md) |
| 四種腳本類別專屬限制 | [rules/script-types.md](rules/script-types.md) |
| 頻率限制 + 商品支援矩陣 | [rules/compatibility.md](rules/compatibility.md) |

### 資料存取
| 需求 | 檔案 |
|------|------|
| GetField / GetQuote / GetSymbolField 語法 | [rules/data-access.md](rules/data-access.md) |
| 欄位字串精確匹配 + 單位後綴 | [rules/field-naming.md](rules/field-naming.md) |
| 技術可行性預審流程 | [rules/feasibility-check.md](rules/feasibility-check.md) |

### 查函數（Grep 搜尋 `functions/`）
| 類別 | 檔案 |
|------|------|
| 一般/數學/交易/日期/字串/欄位/時間/陣列 | `functions/builtin/*.md` |
| 技術指標/價格/跨頻率/邏輯/趨勢/期權 | `functions/system/*.md` |

### 查欄位名稱（Grep 搜尋 `fields/`）
| 類別 | 檔案 |
|------|------|
| 報價欄位 (132) | `fields/quote/*.md` |
| 資料欄位 (371) | `fields/data/*.md` |
| 選股欄位 (508) | `fields/selection/*.md` |

### 常用模式與陷阱
| 模式 | 檔案 |
|------|------|
| intrabarpersist 逐筆洗價 | [patterns/intrabarpersist.md](patterns/intrabarpersist.md) |
| 張數轉換 IntPortion | [patterns/lot-conversion.md](patterns/lot-conversion.md) |
| 跨頻率取值 | [patterns/cross-frequency.md](patterns/cross-frequency.md) |
| InputKind 下拉選單 | [patterns/inputkind-dict.md](patterns/inputkind-dict.md) |
| Plot vs PlotK | [patterns/plot-bindK.md](patterns/plot-bindK.md) |
| Rank 獨立空間 | [patterns/rank-syntax.md](patterns/rank-syntax.md) |
| GROUP 語法 | [patterns/group-syntax.md](patterns/group-syntax.md) |
| 常見錯誤表 | [patterns/common-pitfalls.md](patterns/common-pitfalls.md) |

### 範例程式碼（按類型查閱）
| 類型 | 檔案 |
|------|------|
| 指標腳本 | `examples/indicator/*.md` |
| 交易腳本 | `examples/trading/*.md` |
| 選股腳本 | `examples/selection/*.md` |
| 警示腳本 | `examples/alert/*.md` |

### XS 語言關鍵字
| 類型 | 檔案 |
|------|------|
| 流程控制 (if/for/while) | [keywords/control-flow.md](keywords/control-flow.md) |
| 資料型別 (input/var/value) | [keywords/data-types.md](keywords/data-types.md) |
| 運算子 (=/<>/and/or/cross) | [keywords/operators.md](keywords/operators.md) |

---

## 搜尋策略

### 1. 快速查詢（Skill 內部索引）
```
Grep pattern="函數或欄位名稱" path="~/.claude/skills/xs-writer/functions/"
Grep pattern="欄位名稱" path="~/.claude/skills/xs-writer/fields/"
```

### 2. 詳細文件查詢（xs-helper GitHub 快取）
xs-helper 來源：https://github.com/mophyfei/xs-helper
本地快取：`~/.cache/xs-helper/xs-helper backup/`

```
# 若快取不存在，先執行同步
Bash "bash ~/.claude/skills/xs-writer/sync.sh"

# 搜尋完整的函數/欄位文件
Grep pattern="欄位名稱" path="~/.cache/xs-helper/xs-helper backup/"
Glob pattern="**/函數名稱.md" path="~/.cache/xs-helper/xs-helper backup/"
```

### 3. 搜尋順序
1. 先查 Skill 精簡索引 → 速度快、token 少
2. 不確定時查 xs-helper 快取 → 完整詳細文件
3. 欄位名稱**永遠**要比對參考文件，不可憑記憶

---

## 自學習規則

### 錯誤記錄
當用戶回報 XS 程式碼錯誤時：
1. 先修正程式碼
2. 將錯誤模式追加到 [learned/error-patterns.md](learned/error-patterns.md)
3. 格式：`### YYYY-MM-DD: 錯誤標題` + 錯誤/原因/修正

### 欄位修正
欄位名稱寫錯時，記錄到 [learned/field-corrections.md](learned/field-corrections.md)

### 用戶技巧
用戶說「記住這個」或分享注意事項時，記錄到 [learned/user-tips.md](learned/user-tips.md)

### 撰寫前檢查
撰寫新程式碼前，先讀取 `learned/error-patterns.md` 檢查是否有相關已知陷阱。

---

## 程式碼註解風格

- **Inputs/Vars**：每行末尾 `//` 說明意義
- **邏輯區塊**：`// ------------------------------` 分隔 + `// N. [中文標題]`
- **關鍵邏輯**：獨立行解釋目的
- **風格**：專業、精確、有條理的中文註解

---

## 自動審查流程（撰寫完成後必須執行）

撰寫完 XS 程式碼後，**必須**逐項執行以下審查，全部通過才能回傳給用戶。
若任一項不通過，**先修正再重新審查**，直到全部通過為止。

### Step 1：語法合規性審查
- [ ] **純 XS 語法**：逐行檢查，確認每個關鍵字、函數都是 XS 原生語法
- [ ] **禁止項目清單**：未使用 `==`、`!=`、`++`、`--`、`+=`、`def`、`function`、`return`（XS 用 `ret`）、`print`（XS 用 `Print`）、`elif`、`else if`（XS 用 `else`）、`switch/case`、`try/catch`、`null/None/nil`、`true/false`（XS 用 `True/False`）、`MarketPosition`、`EntryPrice`、`LastBarOnChart`
- [ ] **函數存在性**：每個使用到的函數，在 `functions/`、xs-helper 快取、或 `learned/error-patterns.md` 中確認存在且用法正確

### Step 2：命名與格式審查
- [ ] 所有 `input` / `var` 名稱以 `_` 開頭
- [ ] `plot` 與 `PlotK` 未混用
- [ ] `InputKind` 預設值與 Dict 型別匹配

### Step 3：資料存取審查
- [ ] `GetField` 欄位名稱 100% 匹配參考文件（含單位後綴 `(元)`、`(%)`、`(億)` 等）
- [ ] 目標商品在欄位支援範圍內
- [ ] 腳本頻率符合系統限制
- [ ] 未在選股腳本中使用分鐘頻率 `GetField`

### Step 4：腳本類型專屬審查
- [ ] 交易腳本：金額轉張數用 `IntPortion`，以 1000 股為單位
- [ ] 交易腳本：狀態變數用 `intrabarpersist`
- [ ] 交易腳本：取庫存用 `FilledAtBroker`，取成本用 `FilledAvgPrice`（禁止 `EntryPrice`）
- [ ] 交易腳本：`Print` 輸出到檔案必須用 `Print(File("路徑"), ...)`，`File()` 不可存入變數
- [ ] 警示腳本：未使用 `OutputField`（選股專用）
- [ ] 選股腳本：未使用 `GetQuote`（警示/交易專用）

### Step 5：已知陷阱比對
- [ ] 比對 `learned/error-patterns.md` 中的所有已知錯誤，確認未踩坑

### 審查結果輸出
審查全部通過後，在程式碼下方附上：
```
✓ 審查通過：語法合規 / 命名規範 / 資料存取 / 類型限制 / 已知陷阱
```
若有修正，說明修正了什麼。
