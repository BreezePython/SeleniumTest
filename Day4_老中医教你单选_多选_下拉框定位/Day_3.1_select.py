# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/22 22:04
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Day_3.1_select.py

from selenium import webdriver
import time

# 本地文件，根据你们的位置，自行修改
URL = 'file:///D:/Codes_Repository/Python/SeleniumTest/Day4_老中医教你单选_多选_下拉框定位/index.html'

options = webdriver.ChromeOptions()
# 调整窗口大小，主要是为了使减小gif文件大小，方便截图上传
options.add_argument('window-size=650,650')
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)

driver.get(URL)

driver.find_element_by_id('name').send_keys("隔壁老王")
time.sleep(1)

sex = driver.find_element_by_id('sex')
sex.find_element_by_css_selector("[value='男']").click()
# driver.find_element_by_xpath('//*[@id="sex"]/option[2]').click()
time.sleep(1)

input_tags = driver.find_elements_by_tag_name('input')
for input_tag in input_tags:
    if input_tag.get_attribute('type') == 'radio' and input_tag.get_attribute('value') == '野广告':
        input_tag.click()
time.sleep(1)

input_tags = driver.find_elements_by_tag_name('input')
for input_tag in input_tags:
    if input_tag.get_attribute('type') == 'checkbox' and input_tag.get_attribute('value') != '腰膝酸软':
        input_tag.click()
time.sleep(2)

driver.close()
