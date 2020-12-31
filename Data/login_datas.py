"""
-*- coding: utf-8 -*-
File    : login_datas.py
Version : 0.1
Author  : usrpi
Date    :2020/12/23
"""

# 登录成功
sucess_data = {"phone":"13916686542", "password":"520lemon"}

# 异常场景 手机号格式不正确（大于11位、小于11位、包含其他字符、不在号码段、为空）
phone_data = [
{"phone":"139166865422", "password":"520lemon", "check":"请输入正确的手机号"},
{"phone":"1391668654", "password":"520lemon", "check":"请输入正确的手机号"},
{"phone":"1391668fgfff", "password":"520lemon", "check":"请输入正确的手机号"},
{"phone":"11116686542", "password":"520lemon", "check":"请输入正确的手机号"},
{"phone":"", "password":"520lemon", "check":"请输入手机号"},
{"phone":"13916686542", "password":"", "check":"请输入密码"}
]

# 异常用例 - 手机号未注册 密码错误
noReg_pwdError_data = [
{"phone":"13916686541", "password":"520lemon", "check":"此账号没有经过授权，请联系管理员!"},
{"phone":"13916686542", "password":"520lem", "check":"帐号或密码错误!"}
]