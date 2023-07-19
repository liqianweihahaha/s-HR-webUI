# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:fileCheckPass
# @ide:PyCharm
# @time:2020/10/26  17:35
# 预入职档案审核表单的相关元素
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 预入职档案审核表单的相关按钮封装
class fileCheck(BasePage):
    def __init__(self):
        super().__init__()

        # ’档案审核‘按钮
        self.fileCheckButtonLocator = (By.CSS_SELECTOR, '#updateFileState')

        # 档案状态下拉框：审核通过，审核不通过
        self.fileStatesSelect = (By.CSS_SELECTOR, '#selectStatus')
        # # ’审核通过‘选项
        # self.filePassLocator = Select(self.fileStatesSelect).select_by_value('审核通过')
        # # ‘审核不通过’选项
        # self.fileNotPassLocator = Select(self.fileStatesSelect).select_by_value('审核不通过')

        # 档案审核‘确定’按钮
        self.confirmButtonLocator = (By.CSS_SELECTOR,
                                     'body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')
        # 档案审核‘取消’按钮
        self.cancelButtonLocator = (By.CSS_SELECTOR,
                                    'body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(2) > span')

    # 获取‘档案审核’按钮
    def getFileCheckButton(self):
        return self.get_element(self.fileCheckButtonLocator)

    # 获取‘档案状态下拉框’
    def getFileStateSelect(self):
        return self.get_element(self.fileStatesSelect)

    # # 获取’审核通过‘选项
    # def getFilePass(self):
    #     return self.get_element(self.filePassLocator)
    #
    # # 获取‘审核不通过’按钮
    # def getFileNotPass(self):
    #     return self.get_element(self.fileNotPassLocator)

    # 获取‘确定’按钮
    def getConfirmButton(self):
        return self.get_element(self.confirmButtonLocator)