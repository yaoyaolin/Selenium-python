#!/usr/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('http://www.55haitao.com')
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(5)

driver.find_element_by_xpath("//*/div/p/img[contains(@src,'btn-close')]").click()
driver.find_element_by_class_name("index-top-login").click()
driver.find_element_by_id("username").send_keys('15921877010')
driver.find_element_by_id("pwd_show").send_keys('pppppp')
driver.find_element_by_id("code").click()#自动识别验证码
time.sleep(15)
driver.find_element_by_id("loginbtn").click()


now_handle = driver.current_window_handle
print(now_handle)

time.sleep(10)

driver.find_element_by_xpath("//*/div[@class='index-slider-pointer']/ul/li[3]").click()
time.sleep(3)
print("定位banner光标成功")
driver.find_element_by_xpath("//*/ul[@class='index-banner-slider-pic']/li[3]/a/img").click()
time.sleep(5)
print('点击banner成功')
all_handles = driver.window_handles
driver.switch_to_window(all_handles[0])
time.sleep(5)
print('回到主窗口')
time.sleep(10)

l = []
store1= driver.find_element_by_xpath("//*/div[@id='store1']/*/*/*/*/div/a/img")
l.append(store1)
guanggao1 = driver.find_element_by_xpath("//*/div[@class='index-guanggao-wrap']/div[@class='clearfix']/p/a/img")
l.append(guanggao1)
zhuanyun1 = driver.find_element_by_xpath("//*/div[@id='transport1']/*/*/*/*/div/a/img")
l.append(zhuanyun1)
shangpin1 = driver.find_element_by_xpath("//*/div[@id='sn-main-item0']/ul/li[2]/a/div/img")
l.append(shangpin1)
guanggao2 = driver.find_element_by_xpath("//*/div[@class='index-main-wrap']/div[5]/div/p[2]/a/img")
l.append(guanggao2)
deal1 = driver.find_element_by_xpath("//*/ul[@id='deal_list']/li[3]/h3/a")
l.append(deal1)
# order1 = driver.find_element_by_xpath("//*/ul[@id='showOrder']/li/div/p/a")
l.append(order1)
time.sleep(5)
for i in range(len(l)):
    l[i].click()
    time.sleep(5)
    driver.switch_to_window(all_handles[0])
    time.sleep(5)
time.sleep(5)

#返利商家
# a = driver.find_element_by_xpath("//*/ul[@id='storeNav']/li[4]").click()
# time.sleep(5)
# a.find_element_by_xpath("//*/div[@id='store3']/*/*/*/*/div/a/img").click()
# time.sleep(5)
# driver.switch_to_window(all_handles[0])
# time.sleep(5)

#失败输出错误内容
# time.sleep(3)
# all_handles = driver.window_handles
# for handle in all_handles:
#     if handle == now_handle:
#         driver.switch_to_window(handle)
#
# time.sleep(5)

driver.quit()