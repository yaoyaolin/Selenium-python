#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from __future__ import print_function
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test1')
cur = conn.cursor()

f = open('data2.txt','r')
while True:
    line = f.readline()
    if line:
        line = line.strip('\n')
        line = line.split(',')
        print(line)
        tel = line[0]
        province = line[1]
        city = line[2]
        cell = line[3]
        cur.execute("insert into data13(tel,province,city,cell) values(%s,%s,%s,%s)", [tel, province, city, cell])
    else:
        break

f.close()
cur.close()
conn.commit()
conn.close()

