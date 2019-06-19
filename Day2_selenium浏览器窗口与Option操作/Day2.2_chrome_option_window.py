# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/19 0:02
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : Day2.2_chrome_option_window.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--start-maximized')
# options.add_argument('--window-size=900,600')

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.jianshu.com/u/d23fd5012bed")

driver.quit()

