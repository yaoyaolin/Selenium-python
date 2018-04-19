#!/usr/bin/python
# -*- coding:UTF-8 -*-

import xlrd
class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        print(self.keys)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        print(self.colNum)
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum):
                print(i)
                s = {}
                values = self.table.row_values(j)
                print(values)
                for x in range(self.colNum):
                    print(x)
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
                return r
if __name__ =="__main__":
    excelPath= r"C:\Users\Administrator\PycharmProjects\mypython\login.xls"
    sheetName = "Sheet1"
    data = ExcelUtil(excelPath  ,sheetName)
    print(data.dict_data())

