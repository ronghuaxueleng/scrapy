# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import traceback
from html2md.image import get_image_name
from html2md.db import Note
from html2md.db import Image
from html2md.db import Urls

reload(sys)
sys.setdefaultencoding('utf-8')

class Html2MdPipeline(object):

    def process_item(self, item, spider):
        try:
            print(u"抓取完毕: %s" % item["title"])
            content = item["content"]
            for img in item["images"]:
                path = get_image_name(img)
                Image.insert(
                        url=img,
                        path=path
                        ).execute()
                content = content.replace(img, '../images/%s' % path)
        except Exception:
            e = traceback.format_exc()
        
        try:
            Note.insert(
                title = item["title"],
                url = item["url"],
                content = content,
                ).execute()
        except Exception:
            e = traceback.format_exc()
            print e
        Urls.update(state=1).where(Urls.url == item["url"]).execute()

        return item

