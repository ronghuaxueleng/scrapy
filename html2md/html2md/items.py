# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Html2MdItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    tag = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    images = scrapy.Field()

class Html2MdUrlItem(scrapy.Item):
    url = scrapy.Field()

class Html2MdImageItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()