# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:preEntryButton
# @ide:PyCharm
# @time:2020/10/26  15:20
# 预入职申请相关button
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

# 预入职相关的按钮封装
class preEntryButtons(BasePage):
    def __init__(self):
        super().__init__()   # 继承BasePage的初始化方法，生成driver

        # ‘预入职登记’按钮
        self.preEntryButtonLocator = (By.CSS_SELECTOR,'#qckAddNew')
        # 预入职列表第一条记录--勾选框
        self.firstCheckBoxLocator = (By.CSS_SELECTOR,'#grid >tbody > tr:nth-child(2) > td:nth-child(1)')
        # '提交审核'按钮
        self.submitButtonLocator = (By.CSS_SELECTOR,'#batchSubmitAudited')
        # 提交审核的‘确定’按钮
        self.confirmSubmitLocator = (By.CSS_SELECTOR,'.messenger-actions >span > a')
        # ‘保存’按钮
        self.saveButtonLocator = (By.CSS_SELECTOR,'.shrbtn-primary')
        # '保存并新增'按钮
        self.saveAndAddButtonLocator = (By.CSS_SELECTOR,'#saveNaddNew')
        # '取消'按钮
        self.cancelButtonLocator = (By.CSS_SELECTOR,'#cancel')
        # 保存成功后，表单的‘预入职登记’面包屑
        self.preEntrybreadCrumbLocator = (By.CSS_SELECTOR,'#breadcrumb > li:nth-child(2) > a')

    # 获取‘预入职登记’按钮
    def getPreEntryButton(self):
        return self.get_element(self.preEntryButtonLocator)
    # 获取预入职列表的第一条记录的勾选框
    def getFirstCheckBox(self):
        return self.get_element(self.firstCheckBoxLocator)
    # 获取‘提交审核’按钮
    def getSubmitButton(self):
        return self.get_element(self.submitButtonLocator)
    # 获取提交审核的’确定‘按钮
    def confirmSubmitButton(self):
        return self.get_element(self.confirmSubmitLocator)
    # 获取‘保存’按钮
    def getSaveButton(self):
        return self.get_element(self.saveButtonLocator)
    # 获取‘保存并新增’按钮
    def getSaveAndAddButton(self):
        return self.get_element(self.saveAndAddButtonLocator)
    # 获取‘取消’按钮
    def getCancelButton(self):
        return self.get_element(self.cancelButtonLocator)
    # 获取‘预入职登记’-面包屑
    def getPreEntrybreadCrumb(self):
        return self.get_element(self.preEntrybreadCrumbLocator)


