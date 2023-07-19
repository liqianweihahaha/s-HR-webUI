# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:incomeCertification
# @ide:PyCharm
# @time:2020/10/26  18:32
# 收入证明申请相关button
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

class incomeCerButtons(BasePage):
    def __init__(self):
        super().__init__()

        # '创建收入证明'按钮
        self.createIncomeButton = (By.CSS_SELECTOR,'#addNew')
        # ‘提交工作流’按钮
        self.workFlowSubmitButton = (By.CSS_SELECTOR,'#submit')

        # 点击'提交工作流'弹窗出来的‘确定’按钮
        self.confirmSubmitButton = (By.CSS_SELECTOR,'.messenger-actions > span:nth-child(1) > a')

