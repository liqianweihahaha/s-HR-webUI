# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:smallTools
# @ide:PyCharm
# @time:2020/11/11  16:04
import random
import string
# 一些小工具封装再这里，供测试用例传值时调用

# 随机生成员工姓名
def employName():
    nameTable = ['张三一', '张三二', '张三三']
    name = random.choice(nameTable)
    return name

# 随机生成手机号码
def employTel():
    all_phone_nums = set()
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                 '188','147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 8))
    res = start + end + '\n'
    return res

# 随机生成护照号码
def employPassport():
    passport = random.randint(22222,99999)
    return passport




