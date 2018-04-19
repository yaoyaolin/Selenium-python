#!/usr/bin/python
# -*- coding:UTF-8 -*-
from  selenium import webdriver
import unittest
import time
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://my.dev.55haitao.com/login"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self,name,psw):
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("pwd_show").clear()
        time.sleep(4)
        self.driver.find_element_by_id("pwd").click()
        self.driver.find_element_by_id("pwd").send_keys(psw)
        self.driver.find_element_by_id("loginbtn").click()
        time.sleep(3)

    def is_login_success(self):
        try:
            text = self.driver.find_element_by_xpath("//*[@class='header-login-name']/a").text
            print("a")
            print(text)
            return True
        except:
            return False

    def test_01(self):
        self.login("18000000001","pppppp")
        result = self.is_login_success()
        print(result)
        self.assertTrue(result)

    def test_02(self):
        self.login("18000000003", "pppppp")
        result = self.is_login_success()
        print(result)
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
