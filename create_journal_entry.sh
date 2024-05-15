#!/bin/bash

# 获取当前日期
# DATE=$(date +"%Y-%m-%d %H:%M:%S")

# 获取当前日期和时间，使用 UTC 时间并以 ISO 8601 格式输出
DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# YEAR=$(date +"%Y")

# MONTH=$(date +"%m")

# DAY=$(date +"%d")
YEAR=$(date -u +"%Y")
MONTH=$(date -u +"%m")
DAY=$(date -u +"%d")
DATE_FORMATTED="$YEAR-$MONTH-$DAY"
# 获取当天是星期几

WEEKDAY=$(date +"%A")

# 定义文件路径和文件名

FILE_PATH="content/journal/$YEAR/$MONTH"

FILE_NAME="$DAY.zh.md"

FULL_PATH="$FILE_PATH/$FILE_NAME"

  

# 检查目录是否存在，如果不存在则创建

if [ ! -d "$FILE_PATH" ]; then

mkdir -p "$FILE_PATH"

fi

  

# 创建新的 Markdown 文件并添加一些初始内容

if [ ! -f "$FULL_PATH" ]; then

cat <<EOT >> "$FULL_PATH"
---
title: "$WEEKDAY, $DATE_FORMATTED"
date: "$DATE"
draft: true
---
EOT

echo "Journal entry created at $FULL_PATH"

else

echo "Journal entry already exists at $FULL_PATH"

fi