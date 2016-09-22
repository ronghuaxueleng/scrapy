# -*- coding: utf-8 -*-

import re, sys, os, time
import httplib2
from html2md.db import Urls
from scrapy.selector import Selector
from html2md.settings import START_URL
from html2md.settings import DEFAULT_REQUEST_HEADERS
from html2md.settings import IS_MULTI_PAGE
from html2md.rules import get_urls_rule
from html2md.settings import CONTENT_TYPE


reload(sys)
sys.setdefaultencoding('utf-8')

def get_start_urls():
    start_urls = []
    for url in Urls.select().where(Urls.state != 1).execute():
      start_urls.append(url.url)
    return start_urls


def get_urls():
    if IS_MULTI_PAGE == 'true':
        extract_urls_to_save()
    else:
        row = {
            'title': '',
            'url': START_URL
        }
        save_url(row)

def extract_urls_to_save():
    http = httplib2.Http()  
    response,content = http.request(START_URL,'GET', headers = DEFAULT_REQUEST_HEADERS)
    urls_rule = get_urls_rule(CONTENT_TYPE)
    for item in Selector(text=content).css(urls_rule['body']):
        # 文章链接
        full_url = item.css(urls_rule['a']).extract()[0]
        row = {
            'title': '',
            'url': full_url
        }
        save_url(row)

def save_url(item):
    try:
        Urls.insert(
            title = item["title"],
            url = item["url"],
            state = 0,
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            ).execute()

    except:
        pass

if __name__ == '__main__':
    get_urls()
