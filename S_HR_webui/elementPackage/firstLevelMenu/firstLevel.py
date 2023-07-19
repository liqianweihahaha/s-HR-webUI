# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:firstLevel
# @ide:PyCharm
# @time:2020/10/26  15:16
# 封装一级菜单
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

# 一级菜单封装
class firstLevel(BasePage):
    def __init__(self):
        super().__init__()

        # 菜单名：人力资源共享
        self.sscLocator = (By.CSS_SELECTOR,'#nav-service > li.s-icon-ssc')
        # 菜单名：系统设置
        self.systemSettingLocator = (By.CSS_SELECTOR,'#nav-service > .s-icon-setting')




    # 获取‘人力资源共享’菜单元素
    def getSSCLocator(self):
        return self.get_element(self.sscLocator)
    # 获取‘系统设置’菜单元素
    def getSystemSettingLocator(self):
        return self.get_element(self.systemSettingLocator)

