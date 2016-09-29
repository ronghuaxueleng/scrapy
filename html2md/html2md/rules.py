# -*- coding: utf-8 -*-

import re, sys, os
from scrapy.selector import Selector

reload(sys)
sys.setdefaultencoding('utf-8')

def get_urls_rule(type):
    default_a_rule = 'a::attr(href)'
    rule = {
        'a': default_a_rule,
        'body': ''
    }
    
    if type == 'ryf':
        return multi_page_rule_for_ryf(type, rule)
    elif type == 'cnblogs':
        return multi_page_rule_for_cnblogs(type, rule)
    else:
        return rule

def multi_page_rule_for_ryf(type, rule):
    rule['body'] = '#alpha #alpha-inner .module-categories .module-content .module-list li'
    return rule

def multi_page_rule_for_cnblogs(type, rule):
    rule['body'] = '#mainContent .forFlow #myposts .PostList'
    rule['a'] = 'div > a::attr(href)'
    return rule 


def get_rule(response, type):
    if  type == 'wordpress':
        return wordpress_rule(response)
    elif type == 'githupissues':
        return githup_issues_rule(response)
    elif type == 'ryf':
        return ryf_rule(response)
    elif type == 'cnblogs':
        return cnblogs_rule(response)
    else:
        return {
            'title': '',
            'body': '',
            'images': []
        }
def cnblogs_rule(response):
    title = response.xpath('//*[@id="cb_post_title_url"]/text()').extract()[0]
    body = response.xpath('//*[@id="cnblogs_post_body"]').extract()[0]
    images = re.findall(r'<img\ssrc=["|\'](.*?)["|\']',body)
    return {
        'title': title,
        'body': body,
        'images': images
    }


def ryf_rule(response):
    title = response.xpath('//*[@id="page-title"]/text()').extract()[0]
    body = response.xpath('//*[@id="main-content"]').extract()[0]
    images = re.findall(r'<img\ssrc=["|\'](.*?)["|\']',body)
    return {
        'title': title,
        'body': body,
        'images': images
    }

def githup_issues_rule(response):
    title =  response.xpath('//*[@class="js-issue-title"]/text()|//*[@class=" js-issue-title"]/text()').extract()[0]
    title = title.strip()
    body = response.xpath('//*[@class="comment-body markdown-body markdown-format js-comment-body"]').extract()
    body = '\n'.join(body)
    images = re.findall(r'<img\ssrc=["|\'](.*?)["|\']',body)

    return {
        'title': title,
        'body': body,
        'images': images
    }

def wordpress_rule(response):
    title = response.xpath('//*[@class="entry-title"]/text()').extract()[0]
    title = title.strip()
    body = response.xpath('//*[@class="entry-content clearfix"] | //*[@class="entry-content"]').extract()[0]
    crayon_toolbars = crayon_plains = Selector(text=body).xpath('//div[@class="crayon-toolbar"]').extract()
    for crayon_toolbar in crayon_toolbars:
        body = body.replace(crayon_toolbar,'')
    crayon_plains = Selector(text=body).xpath('//div[@class="crayon-plain-wrap"]').extract()
    for crayon_plain in crayon_plains:
        body = body.replace(crayon_plain,'')
    crayon_nums = Selector(text=body).xpath('//td[@class="crayon-nums "]| //td[@class="crayon-nums"]').extract()
    for crayon_num in crayon_nums:
        body = body.replace(crayon_num,'')
    crayon_codes = Selector(text=body).xpath('//td[@class="crayon-code "]| //td[@class="crayon-code"]').extract()
    for crayon_code in crayon_codes:
        pre = '<pre><code>'+crayon_code+'</code></pre>>'
        body = body.replace(crayon_code,pre)
    images = re.findall(r'<img\ssrc=["|\'](.*?)["|\']',body)
    return {
        'title': title,
        'body': body,
        'images': images
    }
