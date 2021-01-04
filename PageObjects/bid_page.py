"""
-*- coding: utf-8 -*-
File    : bid_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/24
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.bidpage_locators import BidPageLocator as LOC
import logging
from Common.basepage import BasePage

class BidPage(BasePage):

    # def __init__(self, driver):  # 已封装在BasePage类中
    #     self.driver = driver

    # 获取可用余额
    def get_money(self):
        doc = "投资详情页_投资输入框"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.investInput))
        self.wait_eleVisible(LOC.investInput,doc) # 调用BasePage类中元素等待方法
        # money = self.driver.find_element(*LOC.investInput).get_attribute("data-amount") # 获取data-amount的属性值就是可用余额
        money = self.get_attr(LOC.investInput, 'data-amount', doc) # 调用BasePage类中获取元素属性方法
        return float(money)


    # 投标操作
    def invest(self, num):
        doc = "投资详情页_投资操作"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.investInput))
        self.wait_eleVisible(LOC.investInput, doc)  # 调用BasePage类中元素等待方法
        # 输入投资金额
        # self.driver.find_element(*LOC.investInput).send_keys(num)
        self.input_text(LOC.investInput, num, doc) # 调用BasePage类中获取元素输入方法
        # 点击图标按钮
        # self.driver.find_element(*LOC.investButton).click()
        self.click_ele(LOC.investButton, doc) # 调用BasePage类中获取元素点击方法

    # 清除投标金额输入框金额
    def clear_investIput(self):
        self.driver.find_element(*LOC.investInput).clear()

    # 投资成功提示框，点击查看并激活按钮
    def click_activeButton_success_popup(self):
        doc = "投资详情页_投资成功提示框"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.capitalButton))
        self.wait_eleVisible(LOC.capitalButton ,doc)
        # self.driver.find_element(*LOC.capitalButton).click()  # 定位到2个相同元素，选择第二个
        self.click_ele(LOC.capitalButton, doc)

    # 投资错误提示框 -- 页面中间  1.投标金额必须为100的倍数  2.请正确填写投标金额
    def get_erroMsg_from_pageCenter(self):
        doc = "投资详情页_获取页面中间错误提示信息"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.erroMsgCenter))
        self.wait_eleVisible(LOC.erroMsgCenter, doc)
        # return self.driver.find_element(*LOC.erroMsgCenter).text
        return self.get_text(LOC.erroMsgCenter, doc)

    # 关闭错误提示框-- 页面中间  投标金额必须为100的倍数
    def errMsg_button_from_pageCenter(self):
        doc = "投资详情页_关闭页面中间错误提示框"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.erroMsgCenterButton))
        self.wait_eleVisible(LOC.erroMsgCenterButton, doc)
        # self.driver.find_element(*LOC.erroMsgCenterButton).click()
        self.click_ele(LOC.erroMsgCenterButton, doc)

    # 投标按钮错误提示信息   请输入10的倍数
    def get_erroMsg_from_investButton(self, num):
        doc = "投资详情页_获取投标按钮错误提示信息"
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.investInput))
        self.wait_eleVisible(LOC.investInput, doc)
        # 输入投资金额
        # self.driver.find_element(*LOC.investInput).send_keys(num)
        self.input_text(LOC.investInput, num, doc)
        # return self.driver.find_element(*LOC.investButton).text
        return self.get_text(LOC.investButton, doc)