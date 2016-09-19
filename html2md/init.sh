#! /bin/bash

python -c "from html2md.db import init_table; init_table()"

mkdir -p output/markdown 
mkdir -p output/images

echo "[INFO] 完成"
