"""
-*- coding: utf-8 -*-
File    : basepage.py
Version : 0.1
Author  : usrpi
Date    :2021/1/4
"""
import logging
import datetime
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 封装基本函数 -- 执行日志、处理异常、失败截图
# 所有的页面公共部分，不涉及业务
class BasePage:

    def __init__(self, driver):
        self.driver = driver


    # 等待元素可见
    def wait_eleVisible(self, locator, times=30 ,poll_frequency=0.5, doc=""):
        """
        :param locator: 元素定位。 元素形式（元素定位类型、元素定位方式）
        :param times:
        :param poll_frequency:
        :param doc:
        :return:
        """
        logging.info("等待元素 s% 可见", locator)
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            return WebDriverWait(self.driver, times=30 ,poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 求一个插值，写在日志中，就是等待了多久
            logging.info("等待结束，等待时长为：s%", (end-start))
        except:
            logging.exception("等待元素可见失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素可见
    def wait_eleExist(self, locator):
        pass
    # 查找元素
    def get_ele(self, locator, doc = ""):
        logging.info("查找元素: s%", locator)
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise


    # 点击操作
    def click_ele(self, locator, doc = ""):
        # 找元素
        ele = self.get_ele(locator, doc)
        # 元素操作
        logging.info("点击元素：s%", locator)
        try:
           ele.click()
        except:
            logging.exception("元素点击操作失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise
    # 输入操作
    def input_text(self, locator, text , doc = ""):
        # 找元素
        ele = self.get_ele(locator,doc)
        # 输入操作
        logging.info("元素输入：s%",locator)
        try:
           ele.send_keys(text)
        except:
            logging.exception("数据输入失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc = ""):
        # 找元素
        ele = self.get_ele(locator, doc)
        # 获取文本
        try:
            return ele.text
        except:
            logging.exception("获取文本失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_attr(self, locator,attr, doc = ""):
        # 找元素
        ele = self.get_ele(locator, doc)
        # 获取文本
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素属性失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # alter弹窗处理

    # iframe切换

    # 上传操作

    # 滚动条处理
    # 窗口切换

    # 失败截图
    def save_screenshot(self, name):
        # 图片名称：模块名_页面名称_操作名称_时间.png
        path = os.path.dirname(os.path.dirname(__file__)) + '\\Output\screenshots'
        t = datetime.datetime.now()
        file_name = path + t + ".png"
        self.driver.save_screenshot(file_name)
        logging.info("接取网页成功，文件路径为：s%" , file_name)
