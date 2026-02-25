#!/bin/bash
# xs-writer Skill 安裝腳本
# 幫助 AI 撰寫 XQ 全球贏家 XS 腳本語法
# https://github.com/mophyfei/claude-skill-xs-writer

SKILL_DIR="$HOME/.claude/skills/xs-writer"
REPO_URL="https://github.com/mophyfei/claude-skill-xs-writer.git"

echo "========================================="
echo "  xs-writer Skill 安裝程式"
echo "  XQ XS 腳本撰寫助手"
echo "========================================="
echo ""

# 安裝 skill
if [ -d "$SKILL_DIR/.git" ]; then
    echo "[1/3] 已存在，正在更新..."
    cd "$SKILL_DIR" && git pull origin main
elif [ -d "$SKILL_DIR" ]; then
    echo "[1/3] 目錄已存在但非 git repo，正在備份並重新安裝..."
    mv "$SKILL_DIR" "${SKILL_DIR}.backup.$(date +%Y%m%d%H%M%S)"
    git clone "$REPO_URL" "$SKILL_DIR"
else
    echo "[1/3] 正在安裝 xs-writer skill..."
    mkdir -p "$HOME/.claude/skills"
    git clone "$REPO_URL" "$SKILL_DIR"
fi

# 初始化 learned 目錄（從模板複製，不覆蓋已有內容）
echo "[2/3] 初始化自學習目錄..."
mkdir -p "$SKILL_DIR/learned"
for f in error-patterns field-corrections user-tips; do
    if [ ! -f "$SKILL_DIR/learned/${f}.md" ] && [ -f "$SKILL_DIR/learned/${f}.md.template" ]; then
        cp "$SKILL_DIR/learned/${f}.md.template" "$SKILL_DIR/learned/${f}.md"
        echo "  建立 learned/${f}.md"
    fi
done

# 同步 xs-helper 文件
echo "[3/3] 同步 xs-helper 參考文件..."
bash "$SKILL_DIR/sync.sh"

echo ""
echo "========================================="
echo "  安裝完成！"
echo "  重啟 Claude Code 即可使用 xs-writer skill"
echo "========================================="
echo ""
echo "使用方式：在對話中提到 XS、XQ、交易腳本等關鍵字即自動載入"
echo "更新方式：cd $SKILL_DIR && git pull"
