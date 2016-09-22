# -*- coding: utf-8 -*-

import re, sys, os
import time
from settings import PROXIES
from settings import USE_PROXIES
from db import Image
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

images = Image.select().execute()

def get_image_name(url):
    path = os.path.basename(url)
    group = re.findall('\S+\.[jpg|png|gif|jpeg|bmp]+', path)
    if len(group)>0:
        return group[0]
    else:
        return '%s.jpg' % (time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+str(time.time()))


def request_image(url, image_name):
    print(u"正在下载 %s" % image_name)
    try:
        path = 'output/images/%s' % image_name
        if USE_PROXIES == 'true':
            urllib.urlopen(url, proxies=PROXIES)
        data = urllib.urlretrieve(url,path)
        print(u"%s 下载成功" % image_name)
        return True
    except Exception as e:
        print e
        print(u"%s 下载失败" % image_name)
        return False

def request_images():
    for img in images:
        request_image(img.url, img.path)

if __name__ == '__main__':
    request_images()
