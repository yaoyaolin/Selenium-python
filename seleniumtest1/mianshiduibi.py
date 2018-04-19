#coding:utf-8
import json
import xlrd, pymysql
import sys
from imp import reload
reload(sys)
from imp import reload
import csv
import os

# db = pymysql.connect(host='172.16.2.116',user='55haitao_dev',port=3306,password='FZWOOiteWBrVaK7n2umg',db='mysql',use_unicode=True,charset="utf8")
# print('数据库连接成功')
# cursor = db.cursor()
# #查询数据
# count = cursor.execute('select * from mianshi')
# print('countshu:%s'%count)
# # result = cursor.fetchone()
# # print(result)
# cursor.scroll(0,mode='absolute')
# results = cursor.fetchall()
# for r in results:
#     print(r)

#获取表里数据
def mysql_index():
    db = pymysql.connect(host='172.16.2.116',user='55haitao_dev',port=3306,password='FZWOOiteWBrVaK7n2umg',db='mysql',use_unicode=True,charset="utf8")
    print('数据库连接成功')
    cursor = db.cursor()
    count = cursor.execute('select * from mianshi')
    #print('countshu:%s'%count)
    # result = cursor.fetchone()
    # print(result)
    cursor.scroll(0,mode='absolute')
    results = cursor.fetchall()
    return results,count

    # for r in results:
    #     print(r)

#获取excel里数据
def excel_index():
    data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\AMap_adcode_citycode.xlsx')
    sheet = data.sheet_by_index(1)
    nrows = sheet.nrows
    excel =[]
    for nrow in range(1,nrows):
        rowvalue = sheet.row_values(nrow)
        excel.append(rowvalue)
    return excel

cityname = []
adcode = []
citycode = []

#遍历数据表和excel，对比
def duibi():
    my = mysql_index()
    excellist = excel_index()

    len = my[1]
    mysqllist = my[0]
    print(mysqllist[1][1],excellist[1][0])
    print('第一条[0]',mysqllist[0],excellist[0])
    print('第2条[1]',mysqllist[1],excellist[1])
    cityname = []
    adcode = []
    citycode = []
    # for i in range(0,len-1):
    #     if mysqllist[i][1]==excellist[i][0]:















if __name__ =='__main__':
    jieguo = duibi()


