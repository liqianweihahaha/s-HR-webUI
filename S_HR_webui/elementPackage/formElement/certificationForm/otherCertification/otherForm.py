# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:otherForm
# @ide:PyCharm
# @time:2020/10/26  21:27
# 其他证明办理--表单元素
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

class otherCer(BasePage):
    def __init__(self):
        super().__init__()

        # ‘人事业务组织’的弹窗按钮
        self.perBusinessOrgLocator = (By.CSS_SELECTOR,'#OU > div.row-fluid.row-block > div > div > div.col-lg-6.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # ‘人事业务组织’的第一条数据
        self.firstPerBusinessOrgLocator = (By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(3)')
        # ‘姓名’的弹窗按钮
        self.nameLocator = (By.CSS_SELECTOR,'#apply > div.row-fluid.row-block > div:nth-child(1) > div:nth-child(1) > div.col-lg-6.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # ‘姓名’的第一条数据
        self.firstNameLocator = (By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(3)')
        # 证明类型的弹窗按钮
        self.cerTypeLocator = (By.CSS_SELECTOR,'#apply > div.row-fluid.row-block > div:nth-child(2) > div:nth-child(1) > div.col-lg-6.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 证明类型的第一条数据
        self.firstCerTypeLocator = (By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(4)')
        # 申请原因的弹窗按钮
        self.cerReasonLocator = (By.CSS_SELECTOR,'#apply > div.row-fluid.row-block > div:nth-child(2) > div:nth-child(2) > div.col-lg-6.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 申请原因的第一条数据
        self.firstCerReasonLocator = (By.CSS_SELECTOR, 'tbody  > tr:nth-child(2) > td:nth-child(4)')
        # 期望日期时间控件的按钮
        self.expectTimeButtonLocator = (By.CSS_SELECTOR,'#apply > div.row-fluid.row-block > div:nth-child(3) > div:nth-child(1) > div.col-lg-6.field-ctrl > div > div > div.ui-datepicker-icon > img')
        # 期望日期--默认选今天
        self.expectTodayLocator = (By.CSS_SELECTOR, '#ui-datepicker-div > div:nth-child(3) > button:nth-child(1)')