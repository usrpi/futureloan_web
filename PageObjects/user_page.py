"""
-*- coding: utf-8 -*-
File    : user_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/24
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 元素定位
# 可用余额
user_money = '//li[@class="color_sub"]'
# user_money = '//ul[@class="per_list_right"]/li'
# 投资项目
tz_list = '//div[@class="px_card_active"]'
# 第一条交易记录信息
new_tz = '//div[@class="deal_tab_font1"]'

class UserPage:


    def __init__(self, driver):
        self.driver = driver


    # 获取可用余额
    def user_money(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,user_money)))
        text = self.driver.find_element_by_xpath(user_money).text
        money = text.split('元')[0] # 9999500.00元 将 元 切走，只留数字部分
        return float(money)

    # 获取投资项目最新一条交易记录的本金
    def get_tz_list_money(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, tz_list)))
        # 点击投资项目标签
        self.driver.find_element_by_xpath(tz_list).click()
        # 获取第一条交易记录的本金
        text = self.driver.find_element_by_xpath(new_tz).text   # ???定位不到元素
        return float(text)




