#!/usr/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

def login(user,password):
    driver.get('http://www.baidu.com')
    time.sleep(5)
    driver.find_element_by_id('u1').find_element_by_name('tj_login').click()
    time.sleep(10)
    driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(user)
    driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys(password)
    time.sleep(10)
    driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
    return driver

def logout():
    time.sleep(10)
    #driver.find_element_by_id("u_sp").click()
    mouse = driver.find_element_by_class_name("user-name")
    ActionChains(driver).move_to_element(mouse).perform()
    #dr = driver.find_element_by_id("s_user_name_menu")
    driver.find_element_by_class_name("quit").click()
    driver.quit()




if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver=login("1305421822@qq.com","zha4851139")
    print("a")
    time.sleep(10)
    logout()

    print('b')




