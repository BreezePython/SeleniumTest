# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/19 0:02
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : Day2.3_chrome_infobars_incognito.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--incognito')
options.add_argument('--disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.jianshu.com/u/d23fd5012bed")

driver.quit()

