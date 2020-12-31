"""
-*- coding: utf-8 -*-
File    : bidpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2020/12/31
"""
from selenium.webdriver.common.by import By

# 投资页面的元素和定位方式

class BidPageLocator:
    # 元素定位
    # 投标输入框
    investInput = (By.XPATH, '//input[@class="form-control invest-unit-investinput"]')
    # 投标按钮
    investButton = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 投资成功后，查看并激活按钮
    capitalButton = (By.XPATH, '//div[@class="layui-layer-content"]//div[@class="capital_btn"]/button')
    # 投资错误提示框的文本 -- 页面中间  投标金额必须为100的倍数
    erroMsgCenter = (By.XPATH, '//div[@class="text-center"]')
    # 投资错误提示框的确定按钮 -- 页面中间  投标金额必须为100的倍数
    erroMsgCenterButton = (By.XPATH, '//a[@class="layui-layer-btn0"]')