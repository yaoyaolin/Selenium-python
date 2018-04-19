#coding:utf-8
import json
import xlrd, pymysql
import sys
from imp import reload

reload(sys)
from imp import reload
import csv
from selenium import webdriver
import time, unittest, os


def excel_index(colnameindex=0):
    data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\AMap_adcode_citycode.xlsx')
    sheet = data.sheet_by_index(1)
    nrows = sheet.nrows
    colnames=sheet.row_values(colnameindex)
    print(colnames)
    list =[]
    for nrow in range(1,nrows):
        row = sheet.row_values(nrow)
        if row:
            col_l = {}
            col_l[colnames[2]] = row[2]
            list.append(col_l)
    return list

if __name__ =='__main__':
    jieguo = excel_index()
    print(jieguo)



