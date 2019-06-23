# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/23 20:17
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Day5.1_alert&iframe.py

from selenium import webdriver
import time

URL = 'file:///D:/Codes_Repository/Python/SeleniumTest/Day5_alert与iframe定位/index.html'

options = webdriver.ChromeOptions()
options.add_argument('window-size=700,800')
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)

driver.get(URL)
time.sleep(2)
driver.find_element_by_id('access').click()
alert = driver.switch_to.alert
time.sleep(1)
print(alert.text)
alert.accept()
# 由于给定了ifram的name，我们直接可以通过它的name进行定位
driver.switch_to.frame("card")
driver.find_element_by_id('name').send_keys("隔壁老王")
time.sleep(1)
driver.close()
