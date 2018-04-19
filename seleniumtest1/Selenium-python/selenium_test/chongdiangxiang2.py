#coding:utf-8
import json
from bs4 import BeautifulSoup
import requests
import sys
from imp import reload
import csv
reload(sys)


#新增
from selenium import webdriver
import time,unittest,os



#获取多页数据
def url_list():
    urls2 = []
    for i in range(1, 3):
        if i == 1:
            urls = 'https://www.55haitao.com/store/'
            urls2.append(urls)
        else:
            urls = 'https://www.55haitao.com/store/?p={}'.format(str(i))
            urls2.append(urls)
    return urls2


url_list()

# urls = ['https://www.55haitao.com/store/?p={}'.format(str(i)) for i in range(1,5)]
# print(type(urls))
#建立数据存商家名和url
shangjiaite = []


def get_titles(urls, data=None):
    res = requests.get(urls)
    soup = BeautifulSoup(res.text, 'html.parser')
    #shangjiaite = []
    content = soup.find('div', class_='deal-list-main')
    content1 = content.find_all('div', class_='deal-list-store-list')
    #print(type(content1))
    # print(type(content1[0]))
    # 因为content1是列表，所以要取content[0]
    content2 = content1[0].find_all('ul')
    content3 = content2[0].find_all('li')

    # print(len(content1[0].find_all('a')))
    #分有返利和无返利两种url
    for item in content3:
        url = item.find('a', class_='btn-deal-list-store-go show-store-name').get('href')
        text1 = item.find('a', class_='btn-deal-list-store-go show-store-name').text.strip('\r\n\t\ ')
        if text1 == '去购买，拿返利':
            res2 = requests.get(url)
            soup = BeautifulSoup(res2.text, 'html.parser')
            url3 = soup.find('a', class_='btn-go-look').get('href')
            #print(url2)
            s = url3
            try:
                s1 = s.split('=htt')[1].split('%3A%2F%2F')
                s11 = s1[0]
                s12 = s1[1]
                if '%' in s12:
                    s21 = s1[1].split('%')[0]
                    url2 = 'htt' + s11 + '://' + s21
                else:
                    s21 = s1[1].split('&')[0]
                    url2 = 'htt' + s11 + '://' + s21

                    # s1 = s.split('=htt')[1].split('%3A%2F%2F')
                    # s11 = s1[0]
                    # s12 = s1[1].split('%')[0]
                    # url2 = 'htt' + s11 + '://' + s12
            #特殊url处理
            except:
                r = requests.get(s)
                url2 = r.url
        else:
            #无返利的url
            res1 = requests.get(url)
            #print(res1)
            url2 = res1.url

        #新增
        driver = webdriver.Firefox()
        driver.get('http://bbs.55haitao.com/thread-1864068-1-1.html')
        print(driver.title)
        time.sleep(10)






        name = item.find('a').text
        shangjiaite.append([name, url2])


for titles in url_list():
    get_titles(titles)
print(shangjiaite)

# with open('last80.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name', 'url'])
#     for row in shangjiaite:
#         writer.writerow(row)
