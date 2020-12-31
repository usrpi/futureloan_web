"""
-*- coding: utf-8 -*-
File    : invest_datas.py
Version : 0.1
Author  : usrpi
Date    :2020/12/24
"""

# 正确的投资金额
success_num = [300]
# 错误投资金额：不是10的倍数
false_num_no10 = [11,22,33,'ddd','汉字','@##$@!']
# 错误投资金额：不是100的倍数
false_num_no100 = [
    {"num":"0", "check":"请正确填写投标金额"},
    {"num":" ", "check":"请正确填写投标金额"},
    {"num":"-100", "check":"请正确填写投标金额"},
    {"num":"110", "check":"投标金额必须为100的倍数"},
    {"num":"220", "check":"投标金额必须为100的倍数"},
    {"num":"330", "check":"投标金额必须为100的倍数"},
    ]