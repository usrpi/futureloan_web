"""
-*- coding: utf-8 -*-
File    : index_page.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 元素定位
# 第一个抢投标按钮
firstDidButton = '//a[@class="btn btn-special"]'

class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    # 退出 元素
    def isExist_logout_ele(self):
        # 如果元素存在，返回True, 不存在，返回False
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//a[@href="/Index/logout.html"]')))
            return True
        except:
            return False


    # 选择投标
    def select_invest(self):
        # 选择第一个投标
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,firstDidButton)))
        self.driver.find_element_by_xpath(firstDidButton).click()  # 第一二个标已满，选择第三个标