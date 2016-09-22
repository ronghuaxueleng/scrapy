# -*- coding: utf-8 -*-

import re, sys, os, time
import httplib2
from html2md.db import Urls
from scrapy.selector import Selector
from html2md.settings import START_URLS
from html2md.settings import DEFAULT_REQUEST_HEADERS


reload(sys)
sys.setdefaultencoding('utf-8')

def get_start_urls():
    start_urls = []
    for url in Urls.select().where(Urls.state != 1).execute():
      start_urls.append(url.url)
    return start_urls


def get_url():
    get_content(START_URLS)

def get_content(url):
    http = httplib2.Http()  
    response,content = http.request(url,'GET',headers = DEFAULT_REQUEST_HEADERS)
    for item in Selector(text=content).css('#alpha #alpha-inner .module-categories .module-content .module-list li'):
        # 文章链接
        full_url = item.css('a::attr(href)').extract()[0]
        # 文章完整的url
        #full_url = response.urljoin(full_url)
        # 抓文章详情页
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
            timestamp = time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
            ).execute()

    except:
        pass

if __name__ == '__main__':
    headers={}      
    url='http://www.ruanyifeng.com/blog/javascript/'
    get_content(url, headers)
