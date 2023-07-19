# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:预入职正常流程
# @ide:PyCharm
# @time:2020/10/26  21:02
# 流程1：预入职表单提交+档案审核通过+入职单审核通过
# 需要导入：一级菜单、二级菜单、按钮、表单
from elementPackage.firstLevelMenu.firstLevel import firstLevel
from elementPackage.secondLevelMenu.secondLevel import secondLevel
from elementPackage.buttons.preEntryButton.preEntryButton import preEntryButtons
from elementPackage.buttons.preEntryButton.preFileReviewButton import preFileReviewButtons
from elementPackage.buttons.preEntryButton.hiredToHandleButton import hiredToHandleButtons
from elementPackage.formElement.preEntryFormElement.fileCheckForm import fileCheck
from elementPackage.formElement.preEntryFormElement.formSubmission import preEntryForm
from elementPackage.formElement.preEntryFormElement.employeeHiredForm import employeeHired
from utils.smallTools import employName, employTel, employPassport
from time import sleep
import random

# 创建预入职单据
class createPreEmployAction(firstLevel, secondLevel, preEntryButtons, preEntryForm):
    # 创建一条预入职单据
    def createPreEmploy(self):
        # 点击'人力资源共享'一级菜单
        self.getSSCLocator().click()
        # 点击‘预入职登记’ 二级菜单
        self.getPreEntryMenu().click()
        # 点击‘预入职登记’ 按钮
        self.getPreEntryButton().click()
        # 输入‘姓名’--随机姓名
        name = employName()
        self.getName().send_keys(name)
        # 输入手机号码--随机11位
        tel = employTel()
        self.getCellPhone().send_keys(tel)
        # 输入护照号码--随机5位
        passport = employPassport()
        self.getPassport().send_keys(passport)

        # 点击预入职职位按钮
        self.getPreEntryPosition().click()
        # 点击预入职职位弹窗中的第一条数据
        self.getFirstPosition().click()
        sleep(3)

        # 点击人员自助模板按钮
        self.getTemplate().click()
        # 点击人员自助模板中的第一条数据
        self.getFirstTemplate().click()
        sleep(3)

        # 点击保存按钮
        self.getSaveButton().click()
        sleep(3)

        # 点击‘预入职登记’面包屑,回到预入职列表
        self.getPreEntrybreadCrumb().click()
        sleep(3)

        # 勾选第一条记录的勾选框
        self.getFirstCheckBox().click()
        sleep(2)
        # 点击'提交审核'按钮
        self.getSubmitButton().click()
        sleep(2)
        # 点击提交审核的‘确定’按钮
        self.confirmSubmitButton().click()
        sleep(5)
        # 点击home按钮，回到二级菜单页面
        self.driver.find_element_by_css_selector('#breadcrumb > lI > a').click()
        sleep(2)

        # 通过selenium模拟浏览器滚动操作,滚动条滑到最底端
        js = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(6)


# 预入职档案审核
class fileReviewAction(firstLevel, secondLevel, preFileReviewButtons, fileCheck):
    # 审核当前提交的这条单据
    def fileReview(self):
        # 点击预入职档案审核二级菜单
        self.getFileReviewMenu().click()

        # 点击更多按钮
        self.getMoreButton().click()

        # 点击拉取任务
        self.getTaskButton().click()
        sleep(2)
        # 点击‘确定’按钮
        self.getTaskConfirmButton().click()
        sleep(3)

        # 按创建时间倒叙排列
        # 点击两下 创建时间
        self.getCreateTime().click()
        sleep(2)
        self.getCreateTime().click()
        sleep(2)

        # 点击第一条记录
        self.getFirstInformation().click()
        sleep(2)

        # 点击‘审核档案’
        self.getFileCheckButton().click()
        sleep(3)

        # 点击'确定'按钮
        self.getConfirmButton().click()
        sleep(5)

        # 点击home按钮，回到二级菜单页面
        self.driver.find_element_by_css_selector('#breadcrumb > li.homepage > a').click()
        sleep(2)

        # 通过selenium模拟浏览器滚动操作,滚动条滑到最底端
        js = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(6)

# 入职办理
class employeeHiredAction(firstLevel, secondLevel,hiredToHandleButtons,employeeHired):
    # 审核当前提交的这条入职办理记录
    def employeeHired(self):
        # 点击‘入职办理’--二级菜单
        self.getEmployeeHiredMenu().click()

        # # 跳转到入职办理页面
        # self.driver.get('http://172.18.7.94:6888/shr/dynamic.do?uipk=hr.ssc.enrollprocesstasklist&serviceId=e74AAACcikvyPSkQ&inFrame=true')

        # 点击‘更多’按钮
        self.getMoreButton2().click()
        sleep(2)

        # 点击‘拉取任务’按钮
        self.getTaskButtons().click()
        sleep(2)

        # 点击‘确定’按钮
        self.getConfirmButton2().click()
        sleep(2)

        # 点击‘创建时间’两下
        self.getCreateTime2().click()
        sleep(2)
        self.getCreateTime2().click()
        sleep(2)

        # 点击‘入职办理的第一条记录的主题’
        self.getFirstInformation2().click()
        sleep(3)

        # 勾选第一个检查项
        self.getTheFirstCheckItem().click()
        # sleep(1)
        # 勾选第二个检查项
        self.getTheSecondCheckItem().click()
        # sleep(1)
        # 勾选第三个检查项
        self.getTheThirdCheckItem().click()
        # sleep(1)
        # 勾选第四个检查项
        self.getTheFourthCheckItem().click()
        # sleep(1)
        # 勾选第五个检查项
        self.getTheFifthCheckItem().click()
        # sleep(1)
        # 点击 完成检查并入职
        self.getCheckComplete().click()
        sleep(2)

        # 填写 员工编码
        employeeNum = random.randint(11111,99999)
        self.getEmpNumber().send_keys(employeeNum)
        sleep(1)

        # 点击入职日期时间控件
        self.getDateIcon().click()
        # 点击入职日期 中的今天
        self.getToday().click()
        sleep(1)

        # 点击变动类型弹窗
        self.getChangeType().click()
        sleep(1)
        self.getFirstChangeType().click()
        sleep(1)

        # 点击变动原因弹窗
        self.getChangeReason().click()
        sleep(1)
        self.getFirstChangeReason().click()
        sleep(1)

        # 点击员工关系类型
        self.getLabourRelation().click()
        sleep(1)
        self.getFirstLabourRelation().click()
        sleep(1)

        # 点击确定按钮
        self.getSubmitButton().click()

        # 点击确定生成用户弹窗中的--确定按钮
        self.getRetrySubmitButton().click()
        sleep(10)

        # 点击‘入职办理任务列表‘面包屑
        self.getEmployeeHireBreadcrumb().click()



if __name__ == '__main__':
    # 创建预入职单据
    createPreEmployAction().createPreEmploy()
    # 档案审核当前这条单据
    fileReviewAction().fileReview()
    # 入职办理-当前这条单据
    employeeHiredAction().employeeHired()

