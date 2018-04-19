#!/usr/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
#from selenium.commom.exceptions import NoSuchElementException
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
try:
    element = driver.find_element("id","ssu")
except NoSuchElementException as msg:
    print("查找元素异常%s"%msg)
else:
    element.click()