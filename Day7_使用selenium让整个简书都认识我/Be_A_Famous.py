# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/4 02:19
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Be_A_Famous.py


import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
    ElementNotInteractableException, TimeoutException


class FamousPerson:
    # 简书首页地址
    BaseUrl = "https://www.jianshu.com"
    # 脚本目录
    BaseDir = os.path.dirname(os.path.realpath(__file__))
    # 日志文件
    text_name = 'comment.txt'
    # 默认评论页面数
    Page = 3
    # 设置变量，定位已访问的文章数目
    ContentNo = 0

    def __init__(self):
        self.log_text = os.path.join(self.BaseDir, self.text_name)
        self.log_list = self.get_log()
        self.driver = self.init_driver()
        self.base_handle = None
        self.note_list = []

    def get_log(self):
        if os.path.exists(self.log_text):
            with open(self.log_text, 'r', encoding='utf-8') as f:
                return f.readlines()
        return []

    @staticmethod
    def init_driver():
        """
        basic option:
            set screen size
            disable info bar
        :return: driver
        """
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=900,600')
        options.add_argument('disable-infobars')
        return webdriver.Chrome(options=options)

    def prepare_work(self):
        """
        1. add cookie
        2. set base handle
        """
        self.driver.get(self.BaseUrl)
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.base_handle = self.driver.current_window_handle

    def control_scrollbar(self):
        """
        use js to control scroll down ...
        """
        _scrollTop = 0
        # 渐进下拉，避免大幅度页面偏移，导致的textarea获取失败...
        for i in range(20):
            _scrollTop += 400
            js = "var q=document.documentElement.scrollTop={}".format(_scrollTop)
            self.driver.execute_script(js)
            time.sleep(0.2)
        # 简书AJax刷新3次后，必须点击一次查看更多，才能继续刷新...
        try:
            self.driver.find_element_by_class_name('load-more').click()
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass

    def add_comment(self):
        # 判断窗口并切换
        for handle in self.driver.window_handles:
            if handle != self.base_handle:
                self.driver.switch_to.window(handle)
            print("访问文章：{}".format(self.driver.title))
        # 滚动至页面底部
        self.control_scrollbar()
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
                ec.presence_of_element_located((By.TAG_NAME, 'textarea')))
            self.driver.find_element_by_tag_name('textarea').send_keys(comment_info)
            self.driver.find_element_by_class_name('btn-send').click()
            print("回复成功")
        except TimeoutException:
            print("回复失败，未找到textarea，蓝瘦...")
        # 为展示效果，等待2秒，使用时可删除...
        time.sleep(1)
        self.driver.close()
        # 切换至主窗口
        self.driver.switch_to.window(self.base_handle)

    def get_content(self):
        while self.Page:
            notes = self.driver.find_elements_by_css_selector('.note-list li')
            for note in notes[self.ContentNo:]:
                try:
                    note_link = note.find_element_by_tag_name('a')
                    note_name = note_link.text + '\n'
                    if note_name in self.log_list:
                        continue
                    self.log_list.append(note_name)
                    note_link.click()
                    time.sleep(1)
                    self.add_comment()
                    self.ContentNo += 1
                except:
                    pass
            self.Page -= 1
            # 下拉刷新一次页面
            self.control_scrollbar()
        with open(self.log_text, 'w') as f:
            f.writelines(self.log_list)


def run():
    # 实例化方法
    start_test = FamousPerson()
    # add cookie set base_handle
    start_test.prepare_work()
    # 启动评论
    start_test.get_content()


if __name__ == '__main__':
    comment_info = ("为作者点赞! 小弟技术公众号 【清风Python】 刚刚创建,"
                    "欢迎大家关注,谢谢支持。")
    cookie = {
        'name': 'remember_user_token',
        # add value by yourself
        'value': ('W1s1ODQ3NDI2XSwiJDJhJDExJDZLMlU3Vi5NN29WcnlCYy9ycC45aXUi....')
    }
    run()
