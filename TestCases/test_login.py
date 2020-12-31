"""
-*- coding: utf-8 -*-
File    : test_login.py
Version : 0.1
Author  : usrpi
Date    :2020/12/22
"""

from selenium import webdriver
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from Data import login_datas as LD
from ddt import ddt ,data

# 数据分离 - Data
# 测试用例 - ddt引用
# 优化执行效率：setupClass, teardownClass, 每条用例间互不影响
# 元素定位分离：元素定位类型和表达式用元组来管理 - PageLocators层   未实现
@ddt
class TestLogin(unittest.TestCase):
    # 在测试类运行之前运行一次,只运行一次
    # 改造用例：1.所有用例运行之前，打开浏览器，访问登录页面
    #          2.每一个页面操作完成后，刷新当前页面清除数据
    #        3.最后一个用例是登录成功的用例  使用序号决定用例执行顺序
    # 改造后效果：每次用例结束后不用关闭重新打开浏览器，可以节省时间

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://120.78.128.25:8765/Index/login.html')
        cls.driver.maximize_window()
        cls.lg = LoginPage(cls.driver)

    # 所有的用例都跑完之后，再关闭浏览器，只运行一次
    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()

    # def setUp(self):   # 改造前，每次用例结束后关闭重新打开浏览器
    #     # 前置
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://120.78.128.25:8765/Index/login.html')
    #     self.lg = LoginPage(self.driver)

    # 每个用例结束后刷新浏览器，以清除输入框数据，方便后面的用例直接数据新数据
    def tearDown(self):
       self.driver.refresh()

    # 正常用例 - 登录成功
    def test_login_2_succes(self):
        # 前置 访问登录页面    -- setup中已实现
        # 步骤 输入用户名和密码，点击登录
        self.lg.login(LD.sucess_data["phone"],LD.sucess_data["password"])
        # 断言 首页当中--能否找到 退出 这个元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

    # 异常用例 - 手机号格式不正确（大于11位、小于11位、为空、包含其他字符、不在号码段） 错误提示信息都在同一个地方，定位方式相同，故写成一条用例
    @data(*LD.phone_data)
    def test_login_0_phone_error(self,data):
        # 前置 访问登录页面    -- setup中已实现
        # 步骤 输入用户名和密码，点击登录
        self.lg.login(data["phone"],data["password"])
        # 断言 出现提示信息：请输入正确的手机号
        # 登陆页面中 - 获取提示框的文本
        # 比对文本内容 与 期望的值 是否相等
        self.assertEqual(self.lg.get_login_erroMsg_from_loginArea(),data["check"])

    # 异常用例 - 手机号未注册 密码错误 错误提示信息都在同一个地方（页面上方悬浮提示），定位方式相同，故写成一条用例
    @data(*LD.noReg_pwdError_data)
    def test_login_1_phoneNoReg_pwdError(self, data):
        # 前置 访问登录页面    -- setup中已实现
        # 步骤 输入用户名和密码，点击登录
        self.lg.login(data["phone"], data["password"])
        # 断言 出现提示信息：xxxx
        # 登陆页面中 - 获取提示框的文本
        # 比对文本内容 与 期望的值 是否相等
        self.assertEqual(self.lg.get_login_erroMsg_from_loginCenter(), data["check"])

