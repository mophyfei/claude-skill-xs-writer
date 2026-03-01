#!/bin/bash
# xs-helper 同步腳本
# 從 GitHub repo 同步最新的 XS 函數/欄位文件，並自動重建 skill field 文件
# 來源：https://github.com/mophyfei/xs-helper

CACHE_DIR="$HOME/.cache/xs-helper"
REPO_URL="https://github.com/mophyfei/xs-helper.git"
SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== xs-helper 同步腳本 ==="
echo ""

# Step 1: Clone or pull xs-helper repo
if [ -d "$CACHE_DIR/.git" ]; then
    echo "[1/3] 正在更新 xs-helper..."
    cd "$CACHE_DIR" && git pull origin master
else
    echo "[1/3] 首次同步，正在 clone xs-helper..."
    mkdir -p "$(dirname "$CACHE_DIR")"
    git clone "$REPO_URL" "$CACHE_DIR"
fi

XS_HELPER_BACKUP="$CACHE_DIR/xs-helper backup"

if [ ! -d "$XS_HELPER_BACKUP" ]; then
    echo "ERROR: xs-helper backup 目錄不存在！"
    exit 1
fi

echo ""
echo "[2/3] 統計欄位文件數量..."
echo "  報價欄位: $(find "$XS_HELPER_BACKUP/報價欄位" -name '*.md' 2>/dev/null | wc -l)"
echo "  資料欄位: $(find "$XS_HELPER_BACKUP/資料欄位" -name '*.md' 2>/dev/null | wc -l)"
echo "  選股欄位: $(find "$XS_HELPER_BACKUP/選股欄位" -name '*.md' 2>/dev/null | wc -l)"
echo "  內建函數: $(find "$XS_HELPER_BACKUP/內建函數" -name '*.md' 2>/dev/null | wc -l)"
echo "  系統函數: $(find "$XS_HELPER_BACKUP/系統函數" -name '*.md' 2>/dev/null | wc -l)"
echo "  合計: $(find "$XS_HELPER_BACKUP" -name '*.md' 2>/dev/null | wc -l)"

echo ""
echo "[3/3] 重建 skill field 文件..."

REBUILD_SCRIPT="$SKILL_DIR/rebuild_fields.py"

if [ -f "$REBUILD_SCRIPT" ]; then
    python3 "$REBUILD_SCRIPT" --xs-helper-dir "$XS_HELPER_BACKUP"
    if [ $? -eq 0 ]; then
        echo ""
        echo "=== 同步完成 ==="
    else
        echo ""
        echo "ERROR: rebuild_fields.py 執行失敗"
        exit 1
    fi
else
    echo "  WARNING: rebuild_fields.py 不存在: $REBUILD_SCRIPT"
    echo "  請手動執行或在 Claude Code 中請求：\"同步 xs-writer 欄位\""
fi

echo "本地路徑: $CACHE_DIR"
