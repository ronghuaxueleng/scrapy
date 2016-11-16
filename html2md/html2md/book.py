# -*- coding: utf-8 -*-

import sys, re
import time, datetime
import commands
from html2md.db import Note

reload(sys)
sys.setdefaultencoding('utf-8')

def multiple_replace(text,adict):
    rx=re.compile('|'.join(map(re.escape,adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat,text)

def export_to_markdown(item):
    #? * / \ < > : " |
    title = item.title
    content = item.content

    markdown_name = multiple_replace(title,{'?':'？','"':'\'','|':'','/':'or','\\':'','<':'','>':'',':':'：'})
    print markdown_name
    try:
        with open('output/markdown/%s.md' % markdown_name, 'w') as f:
            creat_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

            page_header = '---\n'
            page_header += 'title: %s\n' % item.title
            page_header += 'tag: %s\n' % item.tag
            page_header += 'category: %s\n' % item.category
            page_header += 'date: %s\n' % creat_date
            page_header += 'modifiedOn: %s\n' % creat_date
            page_header += '---\n'

            f.write(page_header + content)
            Note.update(state=1).where(Note.content == content).execute()
    except:
        print '生成%s文件时失败' % markdown_name
        pass


def write_readme():
    content = ''
    content += '我的书籍\n'
    content += '========\n\n'
    content += '生成时间: %s\n' % datetime.datetime.now()
    with open('output/README.md', 'w') as f:
        f.write(content)


def write_summary():
    content = '* [我的书籍](markdown/README.md)\n'

    for i in Note.select().execute():
        content += ' - [%s](markdown/%s.md)\n' % (i.title, i.title)

    with open('output/SUMMARY.md', 'w') as f:
        f.write(content)

def gen_markdown():
    write_readme()
    write_summary()
    for item in Note.select().where(Note.state != 1).execute():
        export_to_markdown(item)

