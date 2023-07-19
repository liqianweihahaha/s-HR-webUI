# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:hiredToHandleButton
# @ide:PyCharm
# @time:2020/10/26  15:25
# 入职办理相关button
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

# 入职办理列表 相关的按钮封装
class hiredToHandleButtons(BasePage):
    def __init__(self):
        super().__init__()

        # 刷新 按钮
        self.refreshButtonLocator = (By.CSS_SELECTOR,'#refresh')
        # 更多 按钮
        self.moreButtonLocator = (By.CSS_SELECTOR,'#workAreaDiv > div > div > div.row-fluid.row-block.view_manager_header.hidden-print > div > div:nth-child(2) > div > span > div > button > span')
        # 拉取任务 按钮
        self.getTaskButtonLocator = (By.CSS_SELECTOR,'#activeGetTask  > a')
        # 确定 按钮
        self.confirmButtonLocator = (By.CSS_SELECTOR,'.ui-dialog-buttonset > button > span')

        # '创建时间'倒叙按钮
        self.createTimeLocator = (By.CSS_SELECTOR,'#jqgh_grid_createTime')
        # '入职办理第一条记录'的主题----用例里面默认选择第一条任务
        self.firstInformationLocator = (By.CSS_SELECTOR,'#grid > tbody > tr:nth-child(2) > td:nth-child(3)')

    # 获取刷新按钮
    def getRefreshButton2(self):
        return self.get_element(self.refreshButtonLocator)
    # 获取 更多 按钮
    def getMoreButton2(self):
        return self.get_element(self.moreButtonLocator)
    # 获取 拉取任务 按钮
    def getTaskButtons(self):
        return self.get_element(self.getTaskButtonLocator)
    # 获取 确定 按钮
    def getConfirmButton2(self):
        return self.get_element(self.confirmButtonLocator)
    # 获取‘创建时间’倒叙按钮
    def getCreateTime2(self):
        return self.get_element(self.createTimeLocator)
    # 获取‘入职办理的第一条记录’
    def getFirstInformation2(self):
        return self.get_element(self.firstInformationLocator)

