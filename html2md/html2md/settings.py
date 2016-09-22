# -*- coding: utf-8 -*-


BOT_NAME = 'html2md'

SPIDER_MODULES = ['html2md.spiders']
NEWSPIDER_MODULE = 'html2md.spiders'

LOG_LEVEL = 'ERROR'

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'

PROXIES = {
        'http': 'http://127.0.0.1:1203',
        'https': 'http://127.0.0.1:1203'
    }

ITEM_PIPELINES = {
    'html2md.pipelines.Html2MdPipeline': 300,
}

PAGE_HEADER = {
    'tag': 'javascript',
    'category': 'javascript'
}

IS_MULTI_PAGE = 'true'

CONTENT_TYPE = 'ryf'

START_URLS = 'http://www.ruanyifeng.com/blog/javascript/'
