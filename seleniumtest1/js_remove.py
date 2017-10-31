#!/usr/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
import time,os

driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")

#用js去掉元素属性，填充数值
js = "document.getElementById('train_date').removeAttribute('readonly')"
driver.execute_script(js)
time.sleep(5)
js_value = 'document.getElementById("train_date").value="2017-10-31"'
driver.execute_script(js_value)

time.sleep(10)

driver.quit()