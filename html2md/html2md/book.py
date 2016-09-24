# -*- coding: utf-8 -*-

import sys
import time, datetime
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


def write_readme():
    content = ''
    content += '简书热门\n'
    content += '========\n\n'
    content += '生成时间: %s\n' % datetime.datetime.now()
    with open('output/README.md', 'w') as f:
        f.write(content)


def write_summary():
    content = '* [Jianshu Hot](markdown/README.md)\n'

    for i in Note.select().execute():
        content += ' - [%s](markdown/%s.md)\n' % (i.title, i.slug)

    with open('output/SUMMARY.md', 'w') as f:
        f.write(content)

def gen_markdown():
    #write_readme()
    #write_summary()
    for item in Note.select().where(Note.state != 1).execute():
        export_to_markdown(item)

