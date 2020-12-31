"""
-*- coding: utf-8 -*-
File    : user_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/24
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.userpage_locators import UserPageLocator


class UserPage(UserPageLocator): # 直接继承UserPageLocator类，函数中的元素定位时可以直接使用继承类中的变量名


    def __init__(self, driver):
        self.driver = driver

    # 获取可用余额
    def get_user_money(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.user_money))
        text = self.driver.find_element(*self.user_money).text
        money = text.split('元')[0] # 9999500.00元 将 元 切走，只留数字部分
        return float(money)

    # 获取投资项目最新一条交易记录的本金
    def get_tz_list_money(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.tz_list))
        # 点击投资项目标签
        self.driver.find_element(*self.tz_list).click()
        # 获取第一条交易记录的本金
        text = self.driver.find_element(*self.new_tz).text   # ???定位不到元素
        return float(text)




