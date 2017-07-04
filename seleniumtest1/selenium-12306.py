#!/usr/bin/python
# -*- coding:UTF-8 -*-
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://kyfw.12306.cn/otn/')
driver.implicitly_wait(30)

driver.find_element_by_link_text('车票预订').click()
s=driver.find_element_by_id('fromStation_icon_image')
webdriver.ActionChains(driver).move_to_element(s).perform()
s.click()
driver.find_element_by_xpath("//*[@id='ul_list1']/li[2]").click()

l = driver.find_element_by_id('toStation_icon_image')
webdriver.ActionChains(driver).move_to_element(l).perform()
l.click()
driver.find_element_by_xpath("//*[@id='ul_list1']/li[3]").click()

# driver.find_element_by_xpath(".//*[@id='_ul_station_train_code']/li[2]/label").click()
# driver.find_element_by_xpath("//input[@value='D']").click()
# driver.find_element_by_xpath("//*[text()='D-动车']").click()
driver.find_element_by_xpath("//label[contains(text(),'D-动车')]").click()

driver.quit()