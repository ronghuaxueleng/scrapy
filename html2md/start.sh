#! /bin/bash

echo "删除旧数据 - note"
python -c "from html2md.db import delete_note; delete_note()"

echo "删除旧数据 - notef"
find ./output/markdown -type f -delete

echo "删除旧数据 - image"
python -c "from html2md.db import delete_image; delete_image()"

echo "删除旧数据 - imagef"
find ./output/images -type f -delete

echo "重新抓取中 - note"
scrapy crawl html2md --nolog

echo "重新抓取中 - image"
python -c "from html2md.image import request_images; request_images()"

echo "生成markdown"
python -c "from html2md.book import gen_markdown; gen_markdown()"
