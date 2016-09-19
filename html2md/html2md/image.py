# -*- coding: utf-8 -*-

import re, sys, os
from html2md.settings import PROXIES
from html2md.db import Image
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

images = Image.select().execute()

def get_image_name(url):
    path = os.path.basename(url)
    group = re.findall('\S+\.[jpg|png|gif|jpeg|bmp]+', path)
    return group[0]

def request_image(url):
    image_name = get_image_name(url)
    print(u"正在下载 %s" % image_name)
    try:
        path = 'output/images/%s' % image_name
        #urllib.urlopen(url, proxies=PROXIES)
        data = urllib.urlretrieve(url,path)
        print(u"%s 下载成功" % image_name)
        return True
    except Exception as e:
        print e
        print(u"%s 下载失败" % image_name)
        return False

def request_images():
    return map(request_image, [ i.url for i in images ])

if __name__ == '__main__':
    request_images()
