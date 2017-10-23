#!/usr/bin/python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
#加载Firefox配置
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\3yx53yaf.default'
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)

driver.get("http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=225998&topic_name=ARJ21%E8%AF%95%E9%A3%9E%E6%88%90%E5%8A%9F")
driver.set_window_size(1000,580)
time.sleep(5)

#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(5)
#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
time.sleep(5)
# 聚焦元素
target = driver.find_element_by_class_name("aside-block-title")
driver.execute_script("arguments[0].scrollIntoView();",target)
time.sleep(10)
driver.quit()