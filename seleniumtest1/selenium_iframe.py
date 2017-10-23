#!/usr/bin/python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import os

driver = webdriver.Firefox()
driver.get('http://bbs.55haitao.com/thread-1864068-1-1.html')
print(driver.title)
time.sleep(10)
driver.find_element_by_class_name("icon-plus").click()
time.sleep(10)
driver.find_element_by_id("fast_username").clear()
driver.find_element_by_id("fast_username").send_keys("18000000001")
time.sleep(10)
driver.find_element_by_id("fast_password").clear()
time.sleep(5)
driver.find_element_by_name("password").send_keys("pppppp")
time.sleep(10)
driver.find_element_by_id("btn-login").click()
time.sleep(5)
print(driver.title)

# iframe1 = driver.find_element_by_class_name("pt")
# driver.switch_to.frame(iframe1)
driver.switch_to.frame("e_iframe")
driver.find_element_by_xpath("html/body").send_keys("asasas")
time.sleep(10)
print("a")
driver.switch_to.default_content()
driver.find_element_by_id("thred_keywords").click()
time.sleep(5)
print("b")
driver.quit()