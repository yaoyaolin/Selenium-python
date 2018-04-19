#coding:utf-8
import json
import xlrd,pymysql
import sys
from imp import reload
reload(sys)
from imp import reload
import csv
from selenium import webdriver
import time, unittest, os


#下载excel文件
driver = webdriver.Firefox()
driver.get('http://lbs.amap.com/api/webservice/download')
driver.implicitly_wait(30)
driver.find_element_by_xpath("//div[@class='download_box download_custom']/div[1]/a").click()
print('a')

#连接数据库
data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\AMap_adcode_citycode.xlsx')
sheet = data.sheet_by_index(1)
db = pymysql.connect(host='172.16.2.116',user='55haitao_dev',port=3306,password='FZWOOiteWBrVaK7n2umg',
                     db='mysql',use_unicode=True,charset="utf8")
print('数据库连接成功')
cursor = db.cursor()
cursor.execute("""
    create table if not exists mianshi
    (
        id int(40) primary key auto_increment,
        cityname varchar(80),
        adcode varchar(40),
        citycode varchar(40)
    )""")
print('创建表成功')
sql = '''insert into mianshi(cityname,adcode,citycode) values(%s,%s,%s)'''
#读取excel里的数据
for r in range(1,sheet.nrows):
    cityname = sheet.cell(r,0).value
    adcode = sheet.cell(r,1).value
    citycode = sheet.cell(r,2).value
    values = (cityname,adcode,citycode)
    try:
        cursor.execute(sql,values)
    except Exception as e:
        db.rollback()
        print(str(e))
print('插入数据库成功')
db.commit()
cursor.close()
db.close()




