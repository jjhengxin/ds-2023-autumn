import csv
import pandas as pd
import requests
from lxml import etree
from bs4 import BeautifulSoup

with open('data.csv','w',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)

    writer.writerow(('name','author','number','mark','publish_time','extract'))
    urls = ['https://weread.qq.com/web/category/60000{}'.format(str(i)) for i in range(0,9)]
    for i in range(10, 11):
        urls.append("https://weread.qq.com/web/category/6000{}".format(str(i)))
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    for url in urls:
        html =  requests.get(url,headers=headers)

    # 解析 HTML 内容
        soup = BeautifulSoup(html.text, 'html.parser')
        comment_number = []
        mark = []
        publish_time = []
        extract = []
    # 查找所有 a 标签并获取链接
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:  # 确保链接存在
                print(href)
                if href.startswith('/web/book'):
                    # 跳转到指定书的详情页
                    durl = 'https://weread.qq.com'+href
                    dhtml = requests.get(durl,headers=headers)
                    dselector = etree.HTML(dhtml.text)
                    #如果评分人数不存在
                    if not dselector.xpath("//*[@id='routerView']/div[1]/div[3]/div[2]/div[1]/div/span/text()"):
                        comment_number.append(["NAN"])
                        mark.append(["NAN"])
                        publish_time.append([dselector.xpath("//*[@id='routerView']/div[1]/div[2]/div[2]/div[2]/div/div[3]/span[2]/text()")[0].strip()])
                        extract.append([dselector.xpath("//*[@id='routerView']/div[1]/div[2]/div[1]/div[2]/div[2]/text()")[0].strip()])
                        continue
                    comment_number.append([dselector.xpath("//*[@id='routerView']/div[1]/div[3]/div[2]/div[1]/div/span/text()")[0]])
                    mark_num = dselector.xpath("//*[@id='routerView']/div[1]/div[3]/div[1]/span/text()")
                    #如果评分不存在
                    if not mark_num:
                        mark_num = dselector.xpath("//*[@id='routerView']/div[1]/div[3]/div[2]/div[1]/span/text()")
                    mark_nnum = mark_num[0].strip()
                    if not mark_nnum.endswith("%") :
                        mark_nnum += "%"
                    mark.append([mark_nnum])
                    # 获取出版时间
                    publish_time.append([dselector.xpath("//*[@id='routerView']/div[1]/div[2]/div[2]/div[2]/div/div[3]/span[2]/text()")[0].strip()])
                    # 获取简介
                    extract.append([dselector.xpath("//*[@id='routerView']/div[1]/div[2]/div[1]/div[2]/div[2]/text()")[0].strip()])

        selector = etree.HTML(html.text)
        #在排行榜页获取书名和作者
        infos = selector.xpath("//*[@id='routerView']/div[2]/div[2]/ul/li")
        print(infos)
        count = 0
        for info in infos:
            test1 = info.xpath("./div[1]/div[2]/p[1]/text()")
            test2 = info.xpath("./div[1]/div[2]/p[2]/a/text()")
            print(test1,test2)
            writer.writerow((test1[0],test2[0],comment_number[count][0],mark[count][0],publish_time[count][0],extract[count][0]))
            count += 1
