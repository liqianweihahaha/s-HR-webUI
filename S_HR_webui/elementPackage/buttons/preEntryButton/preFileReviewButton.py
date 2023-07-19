# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:preFileReviewButton
# @ide:PyCharm
# @time:2020/10/26  15:24
# 入职档案审核相关button
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By


# 预入职档案审核列表相关按钮 封装
class preFileReviewButtons(BasePage):
    def __init__(self):
        super().__init__()   # 继承BasePage的初始化方法，生成driver

        # '刷新'按钮
        self.refreshLocator = (By.CSS_SELECTOR,'#refresh')
        # ’暂挂‘按钮
        self.pauseLocator = (By.CSS_SELECTOR,'#pause')
        # '取消暂挂'按钮
        self.cancelPauseLocator = (By.CSS_SELECTOR,'#cancelPause')
        # ‘更多’按钮
        self.moreLocator = (By.CSS_SELECTOR,'.caret')
        # ‘拉取任务’按钮
        self.getTaskLocator = (By.CSS_SELECTOR,'#activeGetTask > a')
        # 任务拉取弹窗的'确定'按钮
        self.getTaskConfirmLocator = (By.CSS_SELECTOR,'.ui-dialog>div:nth-child(3) > div > button:nth-child(1) > span')


        # '创建时间'倒叙按钮
        self.createTimeLocator = (By.CSS_SELECTOR,'#jqgh_grid_createTime')
        # '档案审核第一条记录'的主题 ----用例里面默认点击第一条数据
        self.firstInformationLocator = (By.CSS_SELECTOR,'#grid > tbody > tr:nth-child(2) > td:nth-child(2)')


    # 获取‘刷新’按钮
    def getRefreshButton(self):
        return self.get_element(self.refreshLocator)
    # 获取‘更多’按钮
    def getMoreButton(self):
        return self.get_element(self.moreLocator)
    # 获取‘拉取任务’按钮
    def getTaskButton(self):
        return self.get_element(self.getTaskLocator)
    # 获取‘确定’按钮
    def getTaskConfirmButton(self):
        return self.get_element(self.getTaskConfirmLocator)

    # 获取'创建时间'倒叙按钮
    def getCreateTime(self):
        return self.get_element(self.createTimeLocator)
    # 获取'档案审核第一条记录'的主题
    def getFirstInformation(self):
        return self.get_element(self.firstInformationLocator)




