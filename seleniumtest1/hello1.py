#!/usr/local/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

elem = driver.find_element_by_id('kw')
elem.send_keys("selenium")
time.sleep(3)
elem.send_keys(Keys.ARROW_DOWN)
time.sleep(10)
elem.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
