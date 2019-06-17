# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/17 23:36
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : Day1_FirstDemo.py

# 引入webdriver，不报错代表代表selenium安装成功
from selenium import webdriver
# 演示所需，添加等待时间
import time

# 定义对应浏览器的webdrvier
# 若提示xxxdriver executable needs to be in PATH
# 你忘记下载webdriver,或者没配置好对应的环境变量
# 当然也会有报错版本不匹配的情况发生，那么请调整好你浏览器与Driver的对应版本
# 几种浏览器对应的引入方式
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
driver = webdriver.Chrome()

# 打开浏览器，并在地址栏输入所需访问的网站(我的简书)
driver.get("https://www.jianshu.com/u/d23fd5012bed")

# 等待1秒，看看是否访问成功？
time.sleep(1)

# 退出drvier关闭浏览器
driver.quit()
