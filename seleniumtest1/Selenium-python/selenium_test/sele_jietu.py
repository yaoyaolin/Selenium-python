#!/usr/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):
    def setUp(self):
        url_login = "https://www.baidu.com"
        self.driver = webdriver.Firefox()
        self.driver.get(url_login)
    def test_01(self):
        try:
            self.driver.find_element_by_id("kw").click()

        except Exception as msg:
            print(u"原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("%s.jpg"%nowTime)
            raise
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
