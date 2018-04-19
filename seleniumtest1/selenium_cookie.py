#!/usr/bin/python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Firefox()
dr.implicitly_wait(30)
print(dr.get_cookies())
dr.get("http://my.dev.55haitao.com/login")
time.sleep(3)

# #用验证码登陆 后清除登陆信息cookie变成未登录状态
# dr.find_element_by_id("username").send_keys('18000000001')
# dr.find_element_by_id("pwd_show").clear()
# time.sleep(4)
# dr.find_element_by_id("pwd").click()
# dr.find_element_by_id("pwd").send_keys('pppppp')
# dr.find_element_by_id("loginbtn").click()
# time.sleep(3)
# print(dr.get_cookie(name = 'member'))
# #{'secure': False, 'name': 'member', 'domain': '.55haitao.com', 'path': '/', 'value': 'htma_f19066b718%09d7e3ec7dcf585e329d7cffe8628499e2%0910954809', 'expiry': None, 'httpOnly': False}
# dr.delete_cookie(name='member')
# time.sleep(3)
# dr.refresh()
# time.sleep(3)

#用cookie登陆
c = {'secure': False,
     'name': 'member',
     'domain': '.55haitao.com',
     'path': '/',
     'value': 'htma_f19066b718%09d7e3ec7dcf585e329d7cffe8628499e2%0910954809',
     'expiry': None,
     'httpOnly': False}
dr.add_cookie(c)
dr.refresh()
time.sleep(3)

dr.quit()
