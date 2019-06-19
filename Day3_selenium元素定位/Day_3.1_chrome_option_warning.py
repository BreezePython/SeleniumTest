# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/19 21:40
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Day_3.1_chrome_option_warning.py
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('window-size=800,600')
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)

driver.get("http://www.baidu.com")

# link_text 定位
driver.find_element_by_link_text('新闻').click()
time.sleep(1)
driver.back()

# id 定位
driver.find_element_by_id("kw").send_keys("id 定位|")
time.sleep(1)

# class name 定位
driver.find_element_by_class_name("s_ipt").send_keys("class name 定位|")
time.sleep(1)

# name 定位
driver.find_element_by_name("wd").send_keys("name 定位|")
time.sleep(1)

# css 定位
driver.find_element_by_css_selector("#kw").send_keys("css 定位|")
time.sleep(1)

# xpath 定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys(" xpath 定位|")
time.sleep(1)



driver.quit()
