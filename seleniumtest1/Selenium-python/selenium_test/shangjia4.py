#coding:utf-8
import json
from bs4 import BeautifulSoup
import requests
import sys
from imp import reload
import  csv
reload(sys)

res = requests.get('http://www.shoplooks.com/retailer')
soup = BeautifulSoup(res.text,'lxml')
shangjiaite =[]
for item in soup.find_all('ul', class_='clearfix'):
    for it in item.find_all('li'):
        url = it.find('a').get('href')
        name = it.text.strip('\r\n\t\ ')
        #print(type(name))
        #print("name\t:\t", name)
        #print("url\t:\t", url)
        s = BeautifulSoup(requests.get(url).text,'lxml')
        a = s.find('span', class_='j-total-prod')
        if a != None:
            counts = a.text
            #print("count\t:\t", a.text)
            shangjiaite.append([name,url,counts])
        else:
            #print("count\t:\t", 0)
            shangjiaite.append([name,url,0])
        print(shangjiaite)

# with open('laste.csv','ab+') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name'.encode(),'url'.encode(),'count'.encode()])
#     for row in shangjiaite:
#         writer.writerow(row)

