"""
-*- coding: utf-8 -*-
File    : userpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2020/12/31
"""
from selenium.webdriver.common.by import By

# 个人中心页面的元素和定位方式
class UserPageLocator:
    # 元素定位
    # 可用余额
    user_money = (By.XPATH, '//li[@class="color_sub"]')
    # 投资项目
    tz_list = (By.XPATH, '//div[@class="px_card_active"]')
    # 第一条交易记录信息
    new_tz = (By.XPATH, '//div[@class="deal_tab_font1"]')