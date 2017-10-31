#!/usr/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException
# from selenium.webdriver.common.keys import  Keys
import time,os

data = open("login.txt",'r')
values = data.readlines()
data.close()
print(values)

for value in values:
    username = value.split(",")[0]
    print(username)
    password = value.split(",")[1]
    print(password)
    driver = webdriver.Firefox()
    driver.get('https://my.55haitao.com/login')
    print(driver.title)
    driver.find_element_by_id("username").send_keys(username)
    time.sleep(5)
    driver.find_element_by_id("pwd_show").send_keys(password)
    time.sleep(5)
    # driver.find_element_by_link_text("登录").click()
    driver.find_element_by_xpath("//div[@class='login-box-submit']/button[1]").click()
    # driver.find_element_by_class_name("btn-login").click()
    time.sleep(10)
    print(driver.title)
    driver.quit()
