# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/18 23:50
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : Day2.1_set_window.py

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.jianshu.com/u/d23fd5012bed")

# 最大化浏览器窗口
driver.maximize_window()
time.sleep(1)
# 调整浏览器窗口为900*600
driver.set_window_size(900, 600)
time.sleep(1)

# 退出drvier关闭浏览器
driver.quit()
