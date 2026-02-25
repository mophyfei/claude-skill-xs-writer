#!/bin/bash
# xs-helper 同步腳本
# 從 GitHub repo 同步最新的 XS 函數/欄位文件
# 來源：https://github.com/mophyfei/xs-helper

CACHE_DIR="$HOME/.cache/xs-helper"
REPO_URL="https://github.com/mophyfei/xs-helper.git"

if [ -d "$CACHE_DIR/.git" ]; then
    echo "正在更新 xs-helper..."
    cd "$CACHE_DIR" && git pull origin main
else
    echo "首次同步，正在 clone xs-helper..."
    mkdir -p "$(dirname "$CACHE_DIR")"
    git clone "$REPO_URL" "$CACHE_DIR"
fi

echo ""
echo "xs-helper 同步完成"
echo "本地路徑: $CACHE_DIR"
echo "文件數量: $(find "$CACHE_DIR/xs-helper backup" -name '*.md' 2>/dev/null | wc -l)"
