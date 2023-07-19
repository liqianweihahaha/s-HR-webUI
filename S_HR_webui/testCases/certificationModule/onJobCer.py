# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:在职证明办理全流程
# @ide:PyCharm
# @time:2020/10/26  21:18
# 流程1：
# 创建在职证明
# 在职证明办理
from time import sleep

import pytest
from elementPackage.firstLevelMenu.firstLevel import firstLevel
from elementPackage.secondLevelMenu.secondLevel import secondLevel
from elementPackage.buttons.certificationButton.onJobCertification import onJobButtons
from elementPackage.formElement.certificationForm.onJobCertification.onJobForm import onJob


# 创建在职证明单据
class onJobCerAction(firstLevel, secondLevel, onJobButtons, onJob):
    def createOnJobCer(self):
        # 点击'人力资源共享'一级菜单
        self.getSSCLocator().click()
        # 点击‘在职证明申请’二级菜单
        self.get_element(self.onJobCertificationMenuLocator).click()
        # 点击'创建在职证明'按钮
        self.get_element(self.createOnJobButton).click()
        # 点击‘人事业务组织’按钮
        self.get_element(self.perBusinessOrgLocator).click()
        # 获取‘人事业务组织’的第一条数据
        self.get_element(self.firstPerBusinessOrgLocator).click()
        # 点击‘姓名’的按钮
        self.get_element(self.nameLocator).click()
        # 获取‘姓名’的第一条数据
        self.get_element(self.firstNameLocator).click()
        # 点击‘证明类型’的按钮
        self.get_element(self.cerTypeLocator).click()
        # 获取‘证明类型’的第一条数据
        self.get_element(self.firstCerTypeLocator).click()
        # 点击‘申请原因’的按钮
        self.get_element(self.cerReasonLocator).click()
        # 获取‘申请原因’的第一条数据
        self.get_element(self.firstCerReasonLocator).click()
        # 点击‘期望日期’的按钮
        self.get_element(self.expectTimeButtonLocator).click()
        # 默认点击‘今天’
        self.get_element(self.expectTodayLocator).click()

        sleep(3)
        # 点击‘提交工作流’按钮
        self.get_element(self.workFlowSubmitButton).click()
        sleep(2)
        self.get_element(self.confirmSubmitFlowButton).click()
        sleep(3)

        # 点击左上角的home图标，回到主页面
        self.driver.find_element_by_css_selector('#breadcrumb > li > a').click()
        sleep(2)
        # 滑动鼠标到页面最底部
        js = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(3)

# 在职证明办理流程
class onJobDealAction(firstLevel,secondLevel,):
    def onJobdDeal(self):
        # 点击‘证明办理’二级菜单
        self.get_element(self.certificationDealMenuLocator).click()
        sleep(2)



if __name__ == "__main__":
    # 创建在职证明
    onJobCerAction().createOnJobCer()
    # 在职证明办理
    onJobDealAction().onJobdDeal()



