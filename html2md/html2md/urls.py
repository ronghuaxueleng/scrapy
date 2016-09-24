# -*- coding: utf-8 -*-

import re, sys, os, time
import hashlib
import httplib2
import json
import traceback
from html2md.db import Urls
from scrapy.selector import Selector
from html2md.settings import URLS_DATA_FILE
from html2md.settings import DEFAULT_REQUEST_HEADERS
from html2md.settings import URLS_OBJ
from html2md.rules import get_urls_rule


reload(sys)
sys.setdefaultencoding('utf-8')

def get_start_urls():
    start_urls = []
    for url in Urls.select().where(Urls.state != 1).execute():
    #for url in Urls.select().execute():
      start_urls.append(url.url)
      URLS_OBJ[hashlib.md5(url.url).hexdigest()] = url
    return start_urls


def get_urls():
    try:
        with open(URLS_DATA_FILE, 'r') as f:
            data = json.load(f)
            for d in data:
                urls = d['url']
                multi_page = d['multi_page']
                tag = d['tag']
                category = d['category']
                content_type = d['content_type']
                
                for url in urls:
                    if multi_page == True:
                        extract_urls_to_save(url, content_type, tag, category)
                    else:
                        row = {
                            'title': '',
                            'url': url,
                            'tag': tag,
                            'category': category,
                            'content_type': content_type
                        }
                        save_url(row)
    except Exception:
        e = traceback.format_exc()
        print e
        pass

def extract_urls_to_save(url, content_type, tag, category):
    http = httplib2.Http()  
    response,content = http.request(url,'GET', headers = DEFAULT_REQUEST_HEADERS)
    urls_rule = get_urls_rule(content_type)
    for item in Selector(text=content).css(urls_rule['body']):
        # 文章链接
        full_url = item.css(urls_rule['a']).extract()[0]
        row = {
            'title': '',
            'url': full_url,
            'tag': tag,
            'category': category,
            'content_type': content_type
        }
        save_url(row)

def save_url(item):
    try:
        Urls.insert(
            title = item["title"],
            url = item["url"],
            tag = item["tag"],
            category = item["category"],
            content_type = item["content_type"],
            state = 0,
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            ).execute()

    except:
        pass

if __name__ == '__main__':
    get_urls()
