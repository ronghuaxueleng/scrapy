# -*- coding: utf-8 -*-

import re, sys
from jianshu.db import Image
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

images = Image.select().execute()

def get_image_name(url):
    group = re.findall('\d+-\w+.\w+', url)
    if not group:
        return None
    image_name = group[0]
    if 'imageMogr' in image_name:
        image_name = image_name.replace('?imageMogr2', '.jpg')

    return image_name

def request_image(url):
    image_name = get_image_name(url)
    print(u"正在下载 %s" % image_name)
    try:
        path = 'output/images/%s' % image_name
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
