# -*- coding: utf-8 -*-

import re, sys, os
import time
from settings import PROXIES
from settings import USE_PROXIES
from settings import DEFAULT_REQUEST_HEADERS
from db import Image
import urllib2
import threading
import Queue

reload(sys)
sys.setdefaultencoding('utf-8')

images = Image.select().where(Image.state != 1).execute()


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
        
        req = urllib2.Request(url);
        req.add_header('User-Agent', DEFAULT_REQUEST_HEADERS['User-Agent']);
        req.add_header('Cache-Control', 'no-cache');
        req.add_header('Accept', '*/*');
        req.add_header('Accept-Encoding', 'gzip, deflate');
        req.add_header('Connection', 'Keep-Alive');
        
        if USE_PROXIES == 'true':
            opener = urllib2.build_opener( urllib2.ProxyHandler(PROXIES))
            urllib2.install_opener( opener )

        resp = urllib2.urlopen(req);
         
        respHtml = resp.read();
        path = 'output/images/%s' % image_name
         
        binfile = open(path, "wb");
        binfile.write(respHtml);
         
        binfile.close();
        Image.update(state=1).where(Image.url == url).execute()
        print(u"%s 下载成功" % image_name)
        return True
    except Exception as e:
        print e
        print(u"%s 下载失败" % image_name)
        return False


def fetch_img_func(q):
    while True:
        try:
            # 不阻塞的读取队列数据
            img = q.get_nowait()
            i = q.qsize()
        except Exception, e:
            print e
            break;
        print 'Current Thread Name Runing %s ... 11' % threading.currentThread().name
        request_image(img.url, img.path)

def request_images():
    q = Queue.Queue()
    for img in images:
        #request_image(img.url, img.path)
        q.put(img)
    start = time.time()
    # 可以开多个线程测试不同效果
    t1 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_1")
    t2 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_2")
    t3 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_3")
    t4 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_4")
    t5 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_5")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    end = time.time()
    print 'Done %s ' %  (end-start)

if __name__ == '__main__':
    request_images()
