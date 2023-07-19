# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:formSubmission
# @ide:PyCharm
# @time:2020/10/26  17:34
# 预入职申请表单元素封装
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

class preEntryForm(BasePage):
    def __init__(self):
        super().__init__()

        # 姓名
        self.nameLocator = (By.CSS_SELECTOR,'#name')
        # 手机号码
        self.cellPhoneLocator = (By.CSS_SELECTOR,'#cellPhone')
        # 身份证号码
        self.idCardLocator = (By.CSS_SELECTOR,'#talent_idCardNO')
        # 护照号码
        self.passportLacator = (By.CSS_SELECTOR,'#talent_passportNO')
        # 预入职职位-弹窗按钮
        self.preEntryPositionLocator = (By.CSS_SELECTOR,'#form > div:nth-child(5) > div:nth-child(1) > div.col-lg-6.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 预入职职位弹窗--第一条数据
        self.firstPositionLocator = (By.XPATH, '//*[@id="b9vW5kNAQIKsgj1CpJ8dC3SuYS4="]/td[3]')
        # 人员自助模板-弹窗按钮
        self.templateLocator = (By.CSS_SELECTOR,'#form > div:nth-child(7) > div:nth-child(1) > div.col-lg-6.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 人员自助模板--第一条数据
        self.firstTemplateLocator = (By.XPATH,'//*[@id="MrQAAAAJ1GkhdzwW"]/td[3]')

    # 获取姓名
    def getName(self):
        return self.get_element(self.nameLocator)
    # 获取手机号码
    def getCellPhone(self):
        return self.get_element(self.cellPhoneLocator)
    # 获取身份证号码
    def getIdCard(self):
        return self.get_element(self.idCardLocator)
    # 获取护照号码
    def getPassport(self):
        return self.get_element(self.passportLacator)
    # 获取'预入职职位-弹窗按钮'
    def getPreEntryPosition(self):
        return self.get_element(self.preEntryPositionLocator)
    # 获取‘预入职职位弹窗--第一条数据’
    def getFirstPosition(self):
        return self.get_element(self.firstPositionLocator)
    # 获取‘人员自助模板-弹窗按钮’
    def getTemplate(self):
        return self.get_element(self.templateLocator)
    # 获取‘人员自助模板--第一条数据’
    def getFirstTemplate(self):
        return self.get_element(self.firstTemplateLocator)






