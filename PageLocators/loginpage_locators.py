"""
-*- coding: utf-8 -*-
File    : loginpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2020/12/31
"""
from selenium.webdriver.common.by import By

# 登录页面的元素和定位方式
class LoginPageLocator:
    # 元素定位
    # 手机号输入框
    input_phone = (By.XPATH, "//input[@name='phone']")
    # 密码输入框
    input_pwd = (By.XPATH, "//input[@name='password']")
    # 登录按钮
    login_button = (By.CLASS_NAME, 'btn')
    # 登录输入框处的错误提示信息
    login_erroMsg_from_loginArea = (By.XPATH, "//div[@class='form-error-info']")
    # 登录页面中间的悬浮提示信息
    login_erroMsg_from_loginCenter = (By.XPATH, "//div[@class='layui-layer-content']")