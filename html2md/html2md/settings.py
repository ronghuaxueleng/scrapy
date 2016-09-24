# -*- coding: utf-8 -*-


BOT_NAME = 'html2md'

SPIDER_MODULES = ['html2md.spiders']
NEWSPIDER_MODULE = 'html2md.spiders'

LOG_LEVEL = 'ERROR'

DEFAULT_REQUEST_HEADERS = {
   'Accept': '*/*',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'

USE_PROXIES = 'true'

PROXIES = {
        'http': 'http://127.0.0.1:1203',
        'https': 'http://127.0.0.1:1203'
    }

ITEM_PIPELINES = {
    'html2md.pipelines.Html2MdPipeline': 300,
}

URLS_OBJ = {}

URLS_DATA_FILE = 'urls.json'
