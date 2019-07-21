# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/12 0:42
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : SavePicture.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.jianshu.com/u/d23fd5012bed")
driver.get_screenshot_as_file('BreezePython.png')
driver.close()


