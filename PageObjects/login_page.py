"""
-*- coding: utf-8 -*-
File    : login_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # 登录
    def login(self, phone, password):

        # 输入手机号
        self.driver.find_element_by_xpath("//input[@name='phone']").send_keys(phone)
        # 输入密码
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        # 点击登录按钮
        self.driver.find_element_by_class_name('btn').click()

    # 获取登录输入框处的错误提示信息
    def get_login_erroMsg_from_loginArea(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='form-error-info']")))
        return self.driver.find_element_by_xpath("//div[@class='form-error-info']").text

    # 获取登录页面中间的悬浮提示信息 手机号未注册(此账号没有经过授权，请联系管理员!) 密码错误(帐号或密码错误!)
    def get_login_erroMsg_from_loginCenter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='layui-layer-content']")))
        return self.driver.find_element_by_xpath("//div[@class='layui-layer-content']").text


    # 注册


    # 忘记密码
