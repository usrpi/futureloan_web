"""
-*- coding: utf-8 -*-
File    : indexpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2020/12/31
"""
from selenium.webdriver.common.by import By


class IndexPageLocator:
    # 元素定位
    # 第一个抢投标按钮
    firstDidButton = (By.XPATH, '//a[@class="btn btn-special"]')
    # 退出按钮
    logout = (By.XPATH,'//a[@href="/Index/logout.html"]')