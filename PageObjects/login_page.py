"""
-*- coding: utf-8 -*-
File    : login_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocator

class LoginPage(LoginPageLocator): # 直接继承LoginPageLocator类，函数中的元素定位时可以直接使用继承类中的变量名

    def __init__(self, driver):
        self.driver = driver

    # 登录
    def login(self, phone, password):

        # 输入手机号
        self.driver.find_element(*self.input_phone).send_keys(phone)
        # 输入密码
        self.driver.find_element(*self.input_pwd).send_keys(password)
        # 点击登录按钮
        self.driver.find_element(*self.login_button).click()

    # 获取登录输入框处的错误提示信息
    def get_login_erroMsg_from_loginArea(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_erroMsg_from_loginArea))
        return self.driver.find_element(*self.login_erroMsg_from_loginArea).text

    # 获取登录页面中间的悬浮提示信息 手机号未注册(此账号没有经过授权，请联系管理员!) 密码错误(帐号或密码错误!)
    def get_login_erroMsg_from_loginCenter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_erroMsg_from_loginCenter))
        return self.driver.find_element(*self.login_erroMsg_from_loginCenter).text


    # 注册


    # 忘记密码
