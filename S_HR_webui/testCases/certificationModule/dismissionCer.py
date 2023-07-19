# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:离职证明办理全流程
# @ide:PyCharm
# @time:2020/10/26  21:18
# 流程2：
# 创建离职证明
# 离职证明办理
from time import sleep

from elementPackage.firstLevelMenu.firstLevel import firstLevel
from elementPackage.secondLevelMenu.secondLevel import secondLevel
from elementPackage.buttons.certificationButton.dimissionCertification import dismissCerButtons
from elementPackage.formElement.certificationForm.dimissionCertification.dimissionForm import dismissCer

class dismissionCerAction(firstLevel,secondLevel,dismissCerButtons,dismissCer):
    def createDismisson(self):
        # 点击‘人力资源共享’一级菜单
        self.get_element(self.sscLocator).click()
        # 点击'离职证明办理'
        self.get_element(self.leaveCertificateMenuLocator).click()
        # 点击'创建离职证明'按钮
        self.get_element(self.createDismissButton).click()
        # 点击‘人事业务组织’按钮
        self.get_element(self.perBusinessOrgLocator).click()
        # 获取‘人事业务组织’的第一条数据
        self.get_element(self.firstPerBusinessOrgLocator).click()
        # 点击‘姓名’的弹窗按钮
        self.get_element(self.nameLocator).click()
        # 获取‘姓名’的第一条数据
        self.get_element(self.firstNameLocator).click()
        # 点击‘证明类型’的弹窗按钮
        self.get_element(self.cerTypeLocator).click()
        # 获取‘证明类型’的第一条数据
        self.get_element(self.firstCerTypeLocator).click()
        # 点击‘申请原因’的弹窗按钮
        self.get_element(self.cerReasonLocator).click()
        # 获取‘申请原因’的第一条数据
        self.get_element(self.firstCerReasonLocator).click()
        # 点击‘期望日期’的时间控件按钮
        self.get_element(self.expectTimeButtonLocator).click()
        # 默认点击‘今天’
        self.get_element(self.expectTodayLocator).click()

        # 点击‘提交工作流’按钮
        self.get_element(self.workFlowSubmitButton).click()
        sleep(3)
        # 点击‘确定’按钮
        self.get_element(self.confirmSubmitButton).click()
        sleep(3)


if __name__ == '__main__':
    dismissionCerAction().createDismisson()













