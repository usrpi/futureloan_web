"""
-*- coding: utf-8 -*-
File    : demo.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://120.78.128.25:8765/Index/login.html')

driver.find_element_by_xpath("//input[@name='phone']").send_keys('13916686542')
# 输入密码
driver.find_element_by_xpath("//input[@name='password']").send_keys('520lemon')
# 点击登录按钮
driver.find_element_by_class_name('btn').click()

# 选择第一个投标
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="btn btn-special"]')))

driver.find_element_by_xpath('//a[@class="btn btn-special"]').click()  # 第一个标已满，选择第二个标
sleep(3)
print(
    driver.find_element_by_xpath('//input[@class="form-control invest-unit-investinput"]').get_attribute("data-amount"))
# 输入投标金额
driver.find_element_by_xpath('//input[@class="form-control invest-unit-investinput"]').send_keys(110)
# 点击图标按钮
print(driver.find_element_by_xpath('//button[@class="btn btn-special height_style"]').text)
# 点击查看并激活按钮


