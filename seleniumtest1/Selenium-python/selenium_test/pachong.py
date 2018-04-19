#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib
import requests

page_link = []

# def get_page_link(page_number):
#     for each_number in range(1,page_number):
#         full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/' .format(each_number)
#         wb_data = requests.get(full_url)
#         print('a')
#         soup = BeautifulSoup(wb_data.text,'lxml')
#         for link in soup.select('a.resule_img_a'):
#             page_link.append(link.get('href'))
#             print('c')
#
# get_page_link(30)
# print(page_link)

#1920?u=https%3A%2F%2Fwww.chemistwarehouse.com.au%2F
#&murl=https%3A%2F%2Fwww.esteelauder.com&u1=mqviqj'

s = 'https://click.linksynergy.com/link?id=9CGqNUoKmgs&offerid=556591.11854998542&type=2&murl=https%3A%2F%2Fwww.esteelauder.com&u1=mqvc46'
s1 = s.split('=htt')[1].split('%3A%2F%2F')
s11 = s1[0]
s12 = s1[1]
if '%' in s12:
    s21 = s1[1].split('%')[0]
    s3 = 'htt'+s11+'://'+s21
    print('a')
else:
    s21 = s1[1].split('&')[0]
    s3 = 'htt'+s11+'://'+s21
    print(s3)


