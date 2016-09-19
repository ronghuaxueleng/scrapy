#! /bin/bash

echo "ɾ�������� - note"
python -c "from html2md.db import delete_note; delete_note()"

echo "ɾ�������� - notef"
find ./output/markdown -type f -delete

echo "ɾ�������� - image"
python -c "from html2md.db import delete_image; delete_image()"

echo "ɾ�������� - imagef"
find ./output/images -type f -delete

echo "����ץȡ�� - note"
scrapy crawl html2md --nolog

echo "����ץȡ�� - image"
python -c "from html2md.image import request_images; request_images()"

echo "����markdown"
python -c "from html2md.book import gen_markdown; gen_markdown()"
