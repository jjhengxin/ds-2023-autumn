import csv
import requests
from lxml import etree
import mysql.connector


with open('movie_data.csv','w',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)

    writer.writerow(('name','actor','information','rate','introduction'))
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
    headers = {
        'User-Agent':'Mozilla/5.0 {X11; Linux x86_64} AppleWebKit/537.36 (KHTML,like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'
}
    
    cnx = mysql.connector.connect(user='ds', password='ds',
                              host='localhost', database='homework04')
    cursor = cnx.cursor()
    insert_query = "INSERT INTO movie_data VALUES (%s,%s,%s,%s,%s)"  # 替换为你的表名和字段名

    for url in urls:
        html =  requests.get(url,headers=headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath("//ol[@class='grid_view']/li")
        
        
        for info in infos:
            name = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a/span[1]/text()")
            
            actor = info.xpath(".//div/div[2]/div[2]/p[1]/text()[1]")
            information = info.xpath(".//div/div[2]/div[2]/p[1]/text()[2]")
            rate = info.xpath(".//div/div[2]/div[2]/div/span[2]/text()")
            introduction = info.xpath(".//div/div[2]/div[2]/p[2]/span/text()")
            if not introduction: 
                introduction=[""]
            writer.writerow((name[0].strip(),actor[0].split('\n')[1].strip(),information[0].strip(),rate[0],introduction[0]))
            cursor.execute(insert_query, (name[0].strip(),actor[0].split('\n')[1].strip(),information[0].strip(),rate[0],introduction[0]))
            cnx.commit()


# 关闭游标和数据库连接
cursor.close()
cnx.close()