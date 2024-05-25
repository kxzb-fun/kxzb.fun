#!/bin/bash

if [ $# -eq 1 ]; then
    DATE_FORMAT=$(date -u +"%Y/%m/$1")
else
    DATE_FORMAT=$(date -u +"%Y/%m/%d")
fi

hugo new journal/"$DATE_FORMAT".zh.md --force # 强制覆盖