#!/usr/bin/python
# -*- coding:UTF-8 -*-
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Firefox()
# driver.get('http://www.55haitao.com')
# driver.implicitly_wait(20)
#
# # now_handle = driver.current_window_handle
# # print(now_handle)
# time.sleep(10)
# #WebDriverWait(driver,10).until(lambda dr:dr.find_element_by_xpath("//*/div[@class='dialog_img']/p/img[@class='btn-close']").click())
#
# # all_handles = driver.window_handles
# driver.find_element_by_xpath("//*/div[@class='dialog_img']/p/img[@class='btn-close']").click()
#
#
# # driver.find_element_by_xpath("//*/div[8]/div/div/div[2]/ul/li[3]/a/img").click()
# #driver.find_element_by_xpath("//*/div[8]/div/div/div[2]/ul/li[4]/a/img").click()
#
# # for handle in all_handles:
# #     if handle == now_handle:
# #         driver.switch_to_window(handle)
# #         driver.close()
#
#
#
#
# driver.quit()



import unittest
class  Test(unittest.TestCase):

    def testMinus(self):
        result = 6-5
        hope = 1
        self.assertEqual(result,hope)

    def testDivide(self):
        result = 6/2
        hope = 2
        self.assertEqual(result,hope)

if __name__ == '__main__':
    unittest.main()
