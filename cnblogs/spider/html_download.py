#coding:utf-8
import urllib2
from Convert.convert import Convert
from spider.html_parse import Html_Parse


class Html_Downloader(object):


    @classmethod
    def download(self,url):

        if url is None:
            return None

        request = urllib2.Request(url)
        request.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0')

        response = urllib2.urlopen(request)

        if response.getcode()!=200:
            return None
        return response.read()


if __name__ == '__main__':
    text = Html_Downloader.download("http://www.cnblogs.com/GongQi/p/4029678.html")
    #print text
    # Html_Parse.parse(text)
    Convert.convert(Html_Parse.parse(text))
    # print text