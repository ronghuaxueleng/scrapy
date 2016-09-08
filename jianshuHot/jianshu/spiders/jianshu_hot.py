# -*- coding: utf-8 -*-
import json
import scrapy
import html2text
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import BaseSgmlLinkExtractor
from jianshu.items import JianshuItem
from jianshu.items import JianshuImageItem


class JianshuHotSpider(CrawlSpider):
    name = "jianshu_hot"
    allowed_domains = ["jianshu.com"]
    start_urls = (
        'http://www.jianshu.com/',
    )

    def parse(self, response):
        for item in response.css('.article-list li'):
            # 文章标题
            # print item.css('h4 a::text').extract()[0].encode('utf-8')
            # 文章链接
            short_url = item.css('h4 a::attr(href)').extract()[0]
            # 文章完整的url
            full_url = response.urljoin(short_url)
            # 抓文章详情页
            yield scrapy.Request(full_url,callback=self.parse_article)

    def parse_article(self, response):
        title = response.xpath('//h1[@class="title"]/text()').extract()[0]
        body = response.xpath('//div[@class="show-content"]').extract()[0]
        attr = response.xpath('//script[@data-name="note"]/text()').extract()
        images = response.xpath('//div[@class="image-package"]/img/@src').extract()
        notes = json.loads(attr[0].strip())

        # 生成markdown 内容
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.inline_links = False
        content = h.handle(body)

        item = JianshuItem()
        item["title"] = title
        item["content"] = content.replace('-\n', '-').replace('\n?', '?')
        item["url"] = notes['url']
        item["slug"] = notes['slug']
        item["views_count"] = notes['views_count']
        item["likes_count"] = notes['likes_count']
        item["images"] = images

        yield item