#coding:utf-8
from Convert.convert import Convert
from spider.html_download import Html_Downloader
from spider.html_parse import Html_Parse


if __name__ == '__main__':
    text = Html_Downloader.download("http://www.cnblogs.com/GongQi/p/4550226.html")
    #print text
    # Html_Parse.parse(text)
    Convert.convert(Html_Parse.parse(text))
    text