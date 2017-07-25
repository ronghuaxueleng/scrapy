#! /bin/bash

path=`pwd`

echo "删除旧数据 - note"
python -c "from jianshu.db import delete_note; delete_note()"

echo "删除旧数据 - notef"
find ./output/markdown -type f -delete

echo "删除旧数据 - image"
python -c "from jianshu.db import delete_image; delete_image()"

echo "删除旧数据 - imagef"
find ./output/images -type f -delete

echo "重新抓取中 - note"
scrapy crawl jianshu_hot --nolog

echo "重新抓取中 - image"
python -c "from jianshu.image import request_images; request_images()"

echo "生成markdown"
python -c "from jianshu.book import gen_markdown; gen_markdown()"

#echo "生成gitbook"
#cd output && gitbook mobi

#echo "处理文件"
#cd $path
#cp output/book.mobi output/books/jianshu_hot-$(date "+%Y%m%d").mobi
#cp output/book.mobi output/books/jianshu_hot-latest.mobi
#echo "完成"


## 自定义邮箱服务器
#YOURKINDLE_MAIL_ADDRESS="xx@kindle.cn"
#YOUR_SEND_MAIL_USERNAME="xx@126.com"
#YOUR_SEND_MAIL_SECRET='xx'
#MOBI_BOOK_PATH=$path'/output/books/jianshu_hot-latest.mobi'

## 定义sendemail命令地址
## -f 表示发送者的邮箱
## -t 表示接收者的邮箱
## -s 表示SMTP服务器的域名或者ip
## -u 表示邮件的主题
## -xu 表示SMTP验证的用户名
## -xp 表示SMTP验证的密码(注意,这个密码貌似有限制,例如我用d!5neyland就不能被正确识别)
## -m 表示邮件的内容
## -cc 表示抄送
## -bcc 表示暗抄送
## -a 表示邮件附件
#$path/sendEmail/sendEmail.exe -s smtp.126.com -t $YOURKINDLE_MAIL_ADDRESS -u "简书热门$(date "+%Y%m%d")" -m "简书热门$(date "+%Y%m%d")" -xu $YOUR_SEND_MAIL_USERNAME -xp $YOUR_SEND_MAIL_SECRET -f $YOUR_SEND_MAIL_USERNAME -a $MOBI_BOOK_PATH -o message-charset=GB2312 -o message-header=GB2312
