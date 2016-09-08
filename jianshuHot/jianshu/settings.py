# -*- coding: utf-8 -*-

BOT_NAME = 'jianshu'

SPIDER_MODULES = ['jianshu.spiders']
NEWSPIDER_MODULE = 'jianshu.spiders'

LOG_LEVEL = 'ERROR'

BLOCK_LIST = (
        'cabc8fa39830'
        )
DOWNLOAD_DELAY=0.25
RANDOMIZE_DOWNLOAD_DELAY = True
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#   'Cache-Control': 'max-age=0',
#   'Connection': 'keep-alive',
#   'Host': 'upload-images.jianshu.io',
#   'If-Modified-Since': 'Wed, 17 Aug 2016 06:15:03 GMT',
#   'If-None-Match': '"AIXV80_6jicRDBHiX05IIxYySaO_"',
#   'Upgrade-Insecure-Requests': 1,
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'

ITEM_PIPELINES = {
    'jianshu.pipelines.JianshuPipeline': 300,
}

