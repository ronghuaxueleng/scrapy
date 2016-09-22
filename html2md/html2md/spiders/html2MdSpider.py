# -*- coding: utf-8 -*-

import sys, re
import json
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import BaseSgmlLinkExtractor
from html2md.items import Html2MdItem
from html2md.items import Html2MdImageItem
from html2md.settings import CONTENT_TYPE
from html2md.rules import get_rule
from html2md.urls import get_start_urls

reload(sys)
sys.setdefaultencoding( "utf-8" )


class Html2MdSpider(CrawlSpider):
    name = "html2md"
    start_urls = get_start_urls()

    def parse(self, response):
        c = get_rule(response, CONTENT_TYPE)

        # 生成markdown 内容

        item = Html2MdItem()
        item["title"] = c['title']
        item["content"] = c['body']
        item["url"] = response.url
        item["images"] = c['images']

        yield item
