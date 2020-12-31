"""
-*- coding: utf-8 -*-
File    : bid_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/24
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.bidpage_locators import BidPageLocator
import logging

class BidPage(BidPageLocator): # 直接继承BidPageLocator类，函数中的元素定位时可以直接使用继承类中的变量名

    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait()


    # 获取可用余额
    def get_money(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.investInput))
            money = self.driver.find_element(*self.investInput).get_attribute("data-amount") # 获取data-amount的属性值就是可用余额
            return float(money)
            logging.INFO(print("获取用户余额成功！！！"))
        except:
            logging.exception("获取用户余额失败！！！")

    # 投标操作
    def invest(self, num):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.investInput))
        # 输入投资金额
        self.driver.find_element(*self.investInput).send_keys(num)
        # 点击图标按钮
        self.driver.find_element(*self.investButton).click()

    # 清除投标金额输入框金额
    def clear_investIput(self):
        self.driver.find_element(*self.investInput).clear()

    # 投资成功提示框，点击查看并激活按钮
    def click_activeButton_success_popup(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.capitalButton))
        self.driver.find_element(*self.capitalButton).click()  # 定位到2个相同元素，选择第二个

    # 投资错误提示框 -- 页面中间  1.投标金额必须为100的倍数  2.请正确填写投标金额
    def get_erroMsg_from_pageCenter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.erroMsgCenter))
        return self.driver.find_element(*self.erroMsgCenter).text

    # 关闭错误提示框-- 页面中间  投标金额必须为100的倍数
    def errMsg_button_from_pageCenter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.erroMsgCenterButton))
        self.driver.find_element(*self.erroMsgCenterButton).click()

    # 投标按钮错误提示信息   请输入10的倍数
    def get_erroMsg_from_investButton(self, num):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.investInput))
        # 输入投资金额
        self.driver.find_element(*self.investInput).send_keys(num)
        return self.driver.find_element(*self.investButton).text