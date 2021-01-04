"""
-*- coding: utf-8 -*-
File    : login_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocator as LOC
from Common.basepage import BasePage


class LoginPage(BasePage):

    # def __init__(self, driver): # 已封装在BasePage类中
    #     self.driver = driver

    # 登录
    def login(self, phone, password):
        doc = "登录页面_登录功能"
        # 输入手机号
        # self.driver.find_element(*LOC.input_phone).send_keys(phone)
        self.input_text(LOC.input_phone,phone,doc)  # 调用BasePage类中输入操作方法
        # 输入密码
        # self.driver.find_element(*LOC.input_pwd).send_keys(password)
        self.input_text(LOC.input_pwd, password, doc)  # 调用BasePage类中输入操作方法
        # 点击登录按钮
        # self.driver.find_element(*LOC.login_button).click()
        self.click_ele(LOC.login_button, doc)  # 调用BasePage类中元素点击方法

    # 获取登录输入框处的错误提示信息
    def get_login_erroMsg_from_loginArea(self):
        doc = "登录页面_登录区域错误提示信息"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.login_erroMsg_from_loginArea))
        self.wait_eleVisible(LOC.login_erroMsg_from_loginArea, doc) # 调用BasePage类中元素等待方法
        # return self.driver.find_element(*LOC.login_erroMsg_from_loginArea).text
        return self.get_text(LOC.login_erroMsg_from_loginArea, doc)  # 调用BasePage类中获取元素文本内容方法

    # 获取登录页面中间的悬浮提示信息 手机号未注册(此账号没有经过授权，请联系管理员!) 密码错误(帐号或密码错误!)
    def get_login_erroMsg_from_loginCenter(self):
        doc = "登录页面_页面中间错误提示信息"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.login_erroMsg_from_loginCenter))
        self.wait_eleVisible(LOC.login_erroMsg_from_loginArea, doc)  # 调用BasePage类中元素等待方法
        # return self.driver.find_element(*LOC.login_erroMsg_from_loginCenter).text
        return self.get_text(LOC.login_erroMsg_from_loginCenter, doc)  # 调用BasePage类中获取元素文本内容方法

    # 注册


    # 忘记密码
