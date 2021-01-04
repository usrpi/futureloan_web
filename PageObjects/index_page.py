"""
-*- coding: utf-8 -*-
File    : index_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.indexpage_locators import IndexPageLocator as LOC
from Common.basepage import BasePage


class IndexPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    # 退出 元素
    def isExist_logout_ele(self):
        # 如果元素存在，返回True, 不存在，返回False
        doc = "主页_退出按钮是否存在"
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LOC.logout))
            self.wait_eleVisible(LOC.logout ,doc)
            return True
        except:
            return False


    # 选择投标
    def select_invest(self):
        doc = "主页_选择投标功能"
        # 选择第一个投标
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LOC.firstDidButton))
        self.wait_eleVisible(LOC.firstDidButton, doc)
        # self.driver.find_element(*LOC.firstDidButton).click()  # 第一二个标已满，选择第三个标
        self.click_ele(LOC.firstDidButton, doc)