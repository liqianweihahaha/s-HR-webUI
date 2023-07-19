# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:onJobCertification
# @ide:PyCharm
# @time:2020/10/26  18:31
# 在职证明申请相关button
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

# 在职证明申请相关button
class onJobButtons(BasePage):
    def __init__(self):
        super().__init__()

        # 创建在职证明--按钮
        self.createOnJobButton = (By.CSS_SELECTOR,'#addEmpBill')
        # 提交工作流--按钮
        self.workFlowSubmitButton = (By.CSS_SELECTOR,'#submit')

        # 点击‘提交工作流’弹窗的‘确定’按钮
        self.confirmSubmitFlowButton = (By.CSS_SELECTOR,'.messenger-actions>span:nth-child(1) >a')

        # 左上角的home图标
        self.toHomeButton = (By.CSS_SELECTOR,'#breadcrumb > lI > a')

