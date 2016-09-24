# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import time
import traceback
import hashlib
import html2text
from html2md.image import get_image_name
from html2md.db import Note
from html2md.db import Image
from html2md.db import Urls

reload(sys)
sys.setdefaultencoding('utf-8')

class Html2MdPipeline(object):

    def process_item(self, item, spider):
        timestamp=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        try:
            print(u"抓取完毕: %s" % item["title"])
            content = item["content"]
            for img in item["images"]:
                try:
                    path = Image.get(Image.url == img).path
                except:
                    path = get_image_name(img)
                    Image.insert(
                        url=img,
                        path=path,
                        state=0,
                        timestamp=timestamp
                        ).execute()

                content = content.replace(img, '../images/%s' % path)
                
        except Exception:
            e = traceback.format_exc()
            print e
            pass
        
        try:
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.inline_links = False
            content = h.handle(content)
            Note.insert(
                title = item["title"],
                url = item["url"],
                tag = item["tag"],
                category = item["category"],
                content = content.replace('-\n', '-').replace('\n?', '?'),
                state=0,
                timestamp=timestamp
                ).execute()
        except Exception:
            e = traceback.format_exc()
            #print e
            pass
        Urls.update(state=1).where(Urls.url == item["url"]).execute()

        return item

