# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:employeeHired
# @ide:PyCharm
# @time:2020/10/26  20:56
# 入职单填写相关的元素
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

# 入职办理表单--相关按钮 和 元素封装
class employeeHired(BasePage):
    def __init__(self):
        super().__init__()

        # 第一个检查项
        self.theFirstCheckItemLocator = (By.CSS_SELECTOR,'#sidebar>div.itembox1 > ol > li:nth-child(1)>span>input')
        # 第二个检查项
        self.theSecondCheckItemLocator = (By.CSS_SELECTOR,'#sidebar>div.itembox1 > ol > li:nth-child(2)>span>input')
        # 第三个检查项
        self.theThirdCheckItemLocator = (By.CSS_SELECTOR, '#sidebar>div.itembox1 > ol > li:nth-child(3)>span>input')
        # 第四个检查项
        self.theFourthCheckItemLocator = (By.CSS_SELECTOR, '#sidebar>div.itembox1 > ol > li:nth-child(4)>span>input')
        # 第五个检查项
        self.theFifthCheckItemLocator = (By.CSS_SELECTOR, '#sidebar>div.itembox1 > ol > li:nth-child(5)>span>input')
        # 完成检查并入职 按钮
        self.checkCompleteLocator = (By.CSS_SELECTOR,'#confirm_entry')

        # 入职单的相关按钮
        # 员工编码 输入框
        self.empNumberLocator = (By.CSS_SELECTOR,'#entrys_empNumber')
        # 入职日期 弹窗按钮
        self.dateIconLocator = (By.CSS_SELECTOR,'#apply > div.row-fluid.row-block > div:nth-child(5) > div:nth-child(1) > div.col-lg-4.field-ctrl > div > div > div.ui-datepicker-icon > img')
        # 入职日期--默认选今天
        self.todayLocator = (By.CSS_SELECTOR,'#ui-datepicker-div > div.ui-datepicker-buttonpane > button.ui-datepicker-current')

        # 变动类型的弹窗按钮
        self.changeTypeLocator = (By.CSS_SELECTOR,'#action > div.row-fluid.row-block > div:nth-child(1) > div:nth-child(2) > div.col-lg-4.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 变动类型弹窗的第一条数据
        self.firstChangeTypeLocator = (By.CSS_SELECTOR,'#list2  > tbody > tr:nth-child(2)  > td:nth-child(4)')
        # 变动原因的弹窗按钮
        self.changeReasonLocator = (By.CSS_SELECTOR,'#action > div.row-fluid.row-block > div:nth-child(1) > div:nth-child(3) > div.col-lg-4.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 变动原因弹窗的第一条数据
        self.firstChangeReasonLocator = (By.CSS_SELECTOR,'#list2 > tbody > tr:nth-child(2) > td:nth-child(4)')
        # 用工关系状态的弹窗按钮
        self.labourRelationLocator = (By.CSS_SELECTOR,'#action > div.row-fluid.row-block > div:nth-child(2) > div > div.col-lg-4.field-ctrl > div > div > div.ui-promptBox-icon > img')
        # 用工关系状态弹窗的第一条数据
        self.firstLabourRelationLocator = (By.CSS_SELECTOR,'#list2 > tbody > tr:nth-child(2) > td:nth-child(4)')

        # 确定按钮
        self.submitButtonLocator = (By.CSS_SELECTOR, '#submitEffect')
        # 确定生成用户弹窗中的--确定按钮
        self.retrySubmitButtonLocator = (By.CSS_SELECTOR,'body > ul > li.messenger-message-slot.shown.first.last > div > div.messenger-actions > span:nth-child(1) > a')

        # 点击‘入职办理任务列表‘面包屑
        self.employeeHireBreadcrumbLocator = (By.CSS_SELECTOR,'#breadcrumb > li:nth-child(2)')

    # 获取第一个检查项
    def getTheFirstCheckItem(self):
        return self.get_element(self.theFirstCheckItemLocator)
    # 获取第二个检查项
    def getTheSecondCheckItem(self):
        return self.get_element(self.theSecondCheckItemLocator)
    # 获取第三个检查项
    def getTheThirdCheckItem(self):
        return self.get_element(self.theThirdCheckItemLocator)
    # 获取第四个检查项
    def getTheFourthCheckItem(self):
        return self.get_element(self.theFourthCheckItemLocator)
    # 获取第五个检查项
    def getTheFifthCheckItem(self):
        return self.get_element(self.theFifthCheckItemLocator)
    # 获取完成检查并入职 按钮
    def getCheckComplete(self):
        return self.get_element(self.checkCompleteLocator)

    # 获取员工编码输入框
    def getEmpNumber(self):
        return self.get_element(self.empNumberLocator)
    # 获取入职日期 弹窗按钮
    def getDateIcon(self):
        return self.get_element(self.dateIconLocator)
    # 获取入职日期---默认选今天
    def getToday(self):
        return self.get_element(self.todayLocator)
    # 获取变动类型的弹窗按钮
    def getChangeType(self):
        return self.get_element(self.changeTypeLocator)
    # 获取变动类型的第一条数据
    def getFirstChangeType(self):
        return self.get_element(self.firstChangeTypeLocator)
    # 获取变动原因的弹窗按钮
    def getChangeReason(self):
        return self.get_element(self.changeReasonLocator)
    # 获取变动原因的第一条数据
    def getFirstChangeReason(self):
        return self.get_element(self.firstChangeReasonLocator)
    # 获取用工关系状态的弹窗按钮
    def getLabourRelation(self):
        return self.get_element(self.labourRelationLocator)
    # 获取用工关系状态弹窗的第一条数据
    def getFirstLabourRelation(self):
        return self.get_element(self.firstLabourRelationLocator)
    # 获取确定按钮
    def getSubmitButton(self):
        return self.get_element(self.submitButtonLocator)
    # 获取 确定生成用户弹窗中的--确定按钮
    def getRetrySubmitButton(self):
        return self.get_element(self.retrySubmitButtonLocator)
    # 获取‘入职办理任务列表‘面包屑
    def getEmployeeHireBreadcrumb(self):
        return self.get_element(self.employeeHireBreadcrumbLocator)

# if __name__ == '__main__':
#     a = employeeHired().getTheFirstCheckItem()
#     print(a)


