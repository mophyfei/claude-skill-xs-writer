# xs-writer — XS 程式碼撰寫 Skill for Claude Code

幫助 AI 撰寫 XQ 全球贏家（XQ Global Winner）的 XS 腳本語法。

## 功能特色

- **四種腳本支援**：指標、交易、選股、警示腳本
- **395 個函數索引**：內建函數 179 個 + 系統函數 216 個
- **1,011 個欄位索引**：報價 132 + 資料 371 + 選股 508
- **自學習機制**：自動記錄錯誤模式，避免重複犯錯
- **GitHub 同步**：從 xs-helper 拉取最新函數/欄位文件
- **精選範例**：各類腳本的實戰程式碼範例

## 安裝方式

### 方法一：一行指令安裝

```bash
git clone https://github.com/mophyfei/claude-skill-xs-writer.git ~/.claude/skills/xs-writer
```

### 方法二：使用安裝腳本（含 xs-helper 同步）

```bash
curl -sSL https://raw.githubusercontent.com/mophyfei/claude-skill-xs-writer/main/install.sh | bash
```

### 方法三：手動安裝

1. 下載本 repo
2. 將整個資料夾放到 `~/.claude/skills/xs-writer/`
3. 重啟 Claude Code

## 使用方式

在 Claude Code 對話中提到以下關鍵字，Skill 會自動載入：

`XS`、`XQ`、`XScript`、`交易腳本`、`指標腳本`、`選股腳本`、`警示腳本`、`GetField`、`GetQuote`、`SetPosition`、`plot`、`PlotK`、`自動交易`、`技術指標撰寫`

## 目錄結構

```
xs-writer/
├── SKILL.md              # 核心規則 + 檔案索引 + 搜尋策略
├── sync.sh               # 同步 xs-helper 最新文件
├── install.sh            # 安裝腳本
├── README.md             # 本說明文件
│
├── rules/                # 撰寫規則
│   ├── syntax-basics.md  # 命名規範、運算子
│   ├── script-types.md   # 四種腳本類別限制
│   ├── data-access.md    # GetField/GetQuote/GetSymbolField
│   ├── field-naming.md   # 欄位字串精確匹配
│   ├── compatibility.md  # 頻率/商品支援矩陣
│   └── feasibility-check.md
│
├── patterns/             # 常用模式與陷阱
│   ├── intrabarpersist.md
│   ├── lot-conversion.md
│   ├── cross-frequency.md
│   ├── inputkind-dict.md
│   ├── plot-bindK.md
│   ├── rank-syntax.md
│   ├── group-syntax.md
│   └── common-pitfalls.md
│
├── functions/            # 函數精簡索引
│   ├── builtin/          # 內建函數 (179)
│   └── system/           # 系統函數 (216)
│
├── fields/               # 欄位精簡索引
│   ├── quote/            # 報價欄位 (132)
│   ├── data/             # 資料欄位 (371)
│   └── selection/        # 選股欄位 (508)
│
├── examples/             # 精選範例
│   ├── indicator/        # 指標腳本範例
│   ├── trading/          # 交易腳本範例
│   ├── selection/        # 選股腳本範例
│   └── alert/            # 警示腳本範例
│
├── keywords/             # XS 語言關鍵字
│   ├── control-flow.md
│   ├── data-types.md
│   └── operators.md
│
└── learned/              # 自學習目錄（AI 自動維護）
    ├── error-patterns.md
    ├── field-corrections.md
    └── user-tips.md
```

## 同步 xs-helper

xs-helper 是 XS 函數/欄位的完整文件庫（1,400+ 份文件），由 GitHub Actions 每週自動更新。

```bash
# 首次同步或更新
bash ~/.claude/skills/xs-writer/sync.sh
```

同步後的本地快取位置：`~/.cache/xs-helper/`

來源：https://github.com/mophyfei/xs-helper

## 自學習機制

Skill 會自動記錄遇到的錯誤和用戶回報的注意事項：

- `learned/error-patterns.md` — 錯誤模式與修正方案
- `learned/field-corrections.md` — 欄位名稱修正記錄
- `learned/user-tips.md` — 用戶分享的技巧

這些記錄會在下次撰寫 XS 時自動參考，持續提升撰寫品質。

## 更新

```bash
cd ~/.claude/skills/xs-writer && git pull
```

## 相關資源

- [xs-helper](https://github.com/mophyfei/xs-helper) — XS 完整函數/欄位文件庫
- [XScript Preset](https://github.com/sysjust-xq/xscript_preset) — 官方 XS 範例程式集
- [XS Blocks](https://github.com/sysjust-xq/XS_Blocks/) — 量化積木程式集
- [XS Help](https://xshelp.xq.com.tw/XSHelp/) — 官方 XS 線上文件

## 授權

MIT License
