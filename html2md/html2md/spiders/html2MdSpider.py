# -*- coding: utf-8 -*-

import sys
import json
import scrapy
import html2text
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import BaseSgmlLinkExtractor
from html2md.items import Html2MdItem
from html2md.items import Html2MdImageItem
import re
reload(sys)
sys.setdefaultencoding( "utf-8" )


class Html2MdSpider(CrawlSpider):
    name = "html2md"
    allowed_domains = ["ruanyifeng.com"]
    start_urls = (
        'http://www.ruanyifeng.com/blog/javascript/',
    )

    def parse(self, response):
        for item in response.css('#alpha #alpha-inner .module-categories .module-content .module-list li'):
            # 文章链接
            full_url = item.css('a::attr(href)').extract()[0]
            # 文章完整的url
            #full_url = response.urljoin(full_url)
            # 抓文章详情页
            yield scrapy.Request(full_url,callback=self.parse_article)

    def parse_article(self, response):
        title = response.xpath('//*[@id="page-title"]/text()').extract()[0]
        body = response.xpath('//*[@id="main-content"]').extract()[0]
        images = re.findall(r'<img\ssrc=["|\'](.*?)["|\']',body)

        # 生成markdown 内容
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.inline_links = False
        content = h.handle(body)

        item = Html2MdItem()
        item["title"] = title
        item["content"] = content.replace('-\n', '-').replace('\n?', '?')
        item["url"] = response.url
        item["images"] = images

        yield item