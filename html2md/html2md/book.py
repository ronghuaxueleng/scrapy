# -*- coding: utf-8 -*-

import sys
import datetime
import commands
from html2md.db import Note

reload(sys)
sys.setdefaultencoding('utf-8')

def export_to_markdown(item):
    #? * / \ < > : " |
    title = item.title
    content = item.content
    markdown_name = title.replace('?','？')
    markdown_name.replace('"','\'').replace('|','')
    markdown_name.replace('|','').replace('*','')
    markdown_name.replace('/','').replace('\\','')
    markdown_name.replace('<','').replace('>','')
    markdown_name.replace(':','：')
    with open('output/markdown/%s.md' % markdown_name, 'w') as f:
        page_header = '---\n'
        page_header += 'title: %s\n' % item.title
        page_header += 'date: %s\n' % datetime.datetime.now()
        page_header += 'modifiedOn: %s\n' % datetime.datetime.now()
        page_header += '---\n'

        f.write(page_header + content)


def write_readme():
    content = ''
    content += '简书热门\n'
    content += '========\n\n'
    content += '生成时间: %s\n' % datetime.datetime.now()
    with open('output/README.md', 'w') as f:
        f.write(content)


def write_summary():
    content = '* [Jianshu Hot](markdown/README.md)\n'

    for i in Note.select().order_by(Note.views_count.desc()).execute():
        content += ' - [%s](markdown/%s.md)\n' % (i.title, i.slug)

    with open('output/SUMMARY.md', 'w') as f:
        f.write(content)

def gen_markdown():
    #write_readme()
    #write_summary()
    for item in Note.select().execute():
        export_to_markdown(item)

