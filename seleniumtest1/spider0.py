#coding=utf-8

from bs4 import BeautifulSoup
import requests
import time

url = "http://news.baidu.com/ns?word=%CE%A2%D0%A6%B5%C4%D0%A1%D0%A1%B5%B6&cl=2&rn=20"
r = requests.get(url)
html = r.text
print(html, "\r\n")
soup = BeautifulSoup(html, 'html.parser')
div_items = soup.find_all('div', class_='result')
print(div_items)
# for div in div_items:
#     a_title = div.find('h3', class_='c-title').find('a').get_text()
#     a_href = div.find('h3', class_='c-title').find('a').get('href')
#     a_summary = div.find('div', class_='c-summary').get_text()
#     now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#     with open('news' + now + '.txt', 'a', ) as file:
#         file.write("标题: " + a_title.encode('utf-8') + "\n")
#         file.write("链接: " + a_href.encode('utf-8') + "\n")
#         file.write("简介: " + a_summary.encode('utf-8') + "\n")

