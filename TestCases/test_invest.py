"""
-*- coding: utf-8 -*-
File    : test_invest.py
Version : 0.1
Author  : usrpi
Date    :2020/12/23
"""
import unittest
from selenium import webdriver
from PageObjects.bid_page import BidPage
from PageObjects.login_page import LoginPage
from PageObjects.user_page import UserPage
from PageObjects.index_page import IndexPage
from Data import login_datas as LD
from Data import invest_datas as ID
from ddt import ddt,data
import logging
# 正常用例
# 前置条件：
# 1.用户已登录
# 2.有能够投资的标   如果没有标，则先加标  # 可用接口方式加标
# 3.有用户余额可以投资

# 操作步骤：
# 1、在首页选标 -- 不根据标名，根据抢投标按钮，默认第一个
#  标页面 - 获取一下用户余额
# 2、标页面 -- 输入投资金额、点击投资按钮
# 3、标页面 -- 点击投资成功的弹出框 - 查看并激活，进入个人页面

# 断言：
# 钱 - 投资后的余额，是不是少了投资的量
# 个人页面 - 获取投资后的金额
# 投资前的金额 - 投资后的金额 = 投资金额
# 投资记录对不对
# 利息对不对？   ----不用断言这个
@ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://120.78.128.25:8765/Index/login.html')
        cls.driver.maximize_window()
        cls.ip = IndexPage(cls.driver)
        cls.bp = BidPage(cls.driver)
        cls.lp = LoginPage(cls.driver)
        cls.up = UserPage(cls.driver)

        # 登陆账号
        cls.lp.login(LD.sucess_data['phone'], LD.sucess_data['password'])
        # 选择投标
        cls.ip.select_invest()

    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()

    @classmethod
    def tearDown(self):
        # self.bp.clear_investIput()
        pass

    @data(*ID.success_num)
    def test_2_invest_succes(self,data):
        logging.info("********投资用例：正常场景-投资成功********")
        # 操作步骤
        # 2.获取投标输入框的可用余额
        num1 = self.bp.get_money()
        # 3.输入输入投标金额，点击投标按钮
        self.bp.invest(data)
        # 4.点击查看并激活按钮
        self.bp.click_activeButton_success_popup()
        # 获取个人中心可用余额
        num2 = self.up.user_money()
        # 获取投资项目最新一条交易记录的本金
        # num3 =self.up.get_tz_list_money()
        # print(num3)
        # 断言 两个可用余额之差等于投标金额
        self.assertEqual(num1 - num2,data)
        # 断言 投标金额与交易记录本金是否相等
        # self.assertEqual(data,float(num3))

# 异常用例：投资金额不是10整数倍、非数字、特殊字符、负数等  获取投标按钮的提示信息:请输入10的整数倍
    @data(*ID.false_num_no10)
    def test_0_invest_no10(self,data):
        logging.info("********投资用例：异常场景-投资金额不是10整数倍********")
        # 获取投资前的可用余额
        num1 = self.bp.get_money()
        # 获取提示信息
        tex = self.bp.get_erroMsg_from_investButton(data)
        # 获取投资后的可用余额
        num2 = self.bp.get_money()
        self.bp.clear_investIput()
        self.assertEqual(tex,'请输入10的整数倍')
        self.assertEqual(num1 - num2,0)

# 异常用例：投资金额不是100整数倍  获取弹窗提示信息：投标金额必须为100的倍数
# 异常用例：空格、0等  获取弹窗提示信息：投标金额必须为100的倍数
    @data(*ID.false_num_no100)
    def test_1_invest_no100(self,data):
        logging.info("********投资用例：异常场景-投资金额不是100整数倍********")
        # 获取投资前的可用余额
        num1 = self.bp.get_money()
        # 输入金额，点击投标按钮
        self.bp.invest(data["num"])
        # 获取提示信息
        tex = self.bp.get_erroMsg_from_pageCenter()
        # 关闭提示框
        self.bp.errMsg_button_from_pageCenter()
        # 获取投资后的可用余额
        num2 = self.bp.get_money()
        self.bp.clear_investIput()
        self.assertEqual(tex, data["check"])
        self.assertEqual(num1 - num2, 0)

# 异常用例：全投资操作？ 标的可投金额 > 个人余额    --- 一次性全投资，会造成后续用例无法继续执行，这种异常用例可以不写自动化用例，手动去执行即可
         # 投资金额 > 标的可投金额   # 满足这种条件标，用户
