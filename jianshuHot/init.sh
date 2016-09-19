#! /bin/bash
python -c "from jianshu.db import init_table; init_table()"

mkdir -p output/markdown 
mkdir -p output/images
mkdir -p output/books

touch output/README.md
touch output/SUMMARY.md

echo "[INFO] 完成"
