
import csv
import requests
from lxml import etree
import mysql.connector
from bs4 import BeautifulSoup

# with open('movie_data.csv','w',newline='',encoding='utf-8') as fp:
    # writer = csv.writer(fp)

    # writer.writerow(('name','actor','information','rate','introduction'))
urls = ['https://weread.qq.com/web/category/600000']
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
    
    # cnx = mysql.connector.connect(user='ds', password='ds',
    #                           host='localhost', database='homework04')
    # cursor = cnx.cursor()
    # insert_query = "INSERT INTO movie_data VALUES (%s,%s,%s,%s,%s)"  # 替换为你的表名和字段名

for url in urls:
    html =  requests.get(url,headers=headers)

    selector = etree.HTML(html.text)
    infos = selector.xpath("//*[@id='routerView']/div[2]/div[2]/ul/li")
    # print(infos)
    # //*[@id="routerView"]/div[2]/div[2]/ul
    
    # //*[@id="routerView"]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/p[1]
    # //*[@id="routerView"]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/p[2]/a
    # /html/body/div[2]/div[4]/div/div/div/div/div/div/ul   
    # /html/body/div[2]/div[4]/div/div/div/div/div/div/ul/li[1]/a[2]
    # //*[@id="page-series-detail"]/div/div/div/ul/li[1]
    for info in infos:
        test1 = info.xpath("./div[1]/div[2]/p[1]/text()")
        test2 = info.xpath("./div[1]/div[2]/p[2]/a/text()")
        print(test1,test2)

        # //*[@id="page-series-detail"]/div/div/div/ul/li[1]/a[1]
        # name = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a/span[1]/text()")
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
        # /html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
        # actor = info.xpath(".//div/div[2]/div[2]/p[1]/text()[1]")
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]/text()[1]
        #     information = info.xpath(".//div/div[2]/div[2]/p[1]/text()[2]")
        #     rate = info.xpath(".//div/div[2]/div[2]/div/span[2]/text()")
        #     introduction = info.xpath(".//div/div[2]/div[2]/p[2]/span/text()")
        #     if not introduction: 
        #         introduction=[""]
        #     writer.writerow((name[0].strip(),actor[0].split('\n')[1].strip(),information[0].strip(),rate[0],introduction[0]))
        #     cursor.execute(insert_query, (name[0].strip(),actor[0].split('\n')[1].strip(),information[0].strip(),rate[0],introduction[0]))
        #     cnx.commit()

