# -*- coding: utf-8 -*-

import sys, re
import json
import hashlib
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import BaseSgmlLinkExtractor
from scrapy.http import Request, FormRequest
from html2md.items import Html2MdItem
from html2md.items import Html2MdImageItem
from html2md.rules import get_rule
from html2md.urls import get_start_urls
from html2md.settings import URLS_OBJ
from html2md.settings import DEFAULT_REQUEST_HEADERS

reload(sys)
sys.setdefaultencoding( "utf-8" )


class Html2MdSpider(CrawlSpider):
    name = "html2md"
    start_urls = get_start_urls()

    def start_requests(self):
        cookies = {
            'io': 'a27VdCN8grnwB0HmAYMS',
            'gr_user_id': '85505a03-fbb7-4567-bf6e-9037d4b014df',
            'PHPSESSID': 'web2~6e53df309a3edf87842b60e599015e6b',
            'activate_count': 10,
            'gr_session_id_5411b7ab1ae040ed9a4eb4a120a06ead': '1ca7e83a-1cf7-4748-9f01-3a61448fcb55',
            'sf_remember': '7dfcee2967f82373ab2e7afac98daf33'
        }
        for i,url in enumerate(self.start_urls):
            yield Request(url, meta={'cookiejar': i}, callback=self.parse_item, cookies = cookies, headers = DEFAULT_REQUEST_HEADERS)

    def parse_item(self, response):
        c = get_rule(response, URLS_OBJ[hashlib.md5(response.url).hexdigest()].content_type)

        # 生成markdown 内容

        item = Html2MdItem()
        item["title"] = c['title']
        item["content"] = c['body']
        item["url"] = response.url
        item["images"] = c['images']
        item["tag"] = URLS_OBJ[hashlib.md5(response.url).hexdigest()].tag
        item["category"] = URLS_OBJ[hashlib.md5(response.url).hexdigest()].category

        yield item
