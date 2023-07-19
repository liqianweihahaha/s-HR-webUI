# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:secondLevel
# @ide:PyCharm
# @time:2020/10/26  15:17
# 二级菜单
from basePages.basePage import BasePage
from selenium.webdriver.common.by import By

# 二级菜单封装
class secondLevel(BasePage):
    def __init__(self):
        super().__init__()

        # 菜单名：预入职登记
        self.preEntryMenuLocator = (By.CSS_SELECTOR,'#home-content-wrap > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div >div')
        # 菜单名：职位入职二维码
        self.qrCodeMenuLocator = (By.CSS_SELECTOR,'#home-content-wrap > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div >div')
        # 菜单名：员工离职共享
        self.employeeTurnOverMenuLocator = (By.CSS_SELECTOR,'#home-content-wrap > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div >div')

        # 菜单名：预入职档案审核
        self.fileReviewMenuLocator = (By.CSS_SELECTOR,'#home-content-wrap > div:nth-child(10) > div:nth-child(2) > div > div:nth-child(1) > div')
        # 菜单名：入职办理
        self.employeeHiredMenuLocator = (By.CSS_SELECTOR,'#home-content-wrap > div:nth-child(10) > div:nth-child(3) > div > div:nth-child(1) > div')

        # 菜单名：在职证明申请
        self.onJobCertificationMenuLocator = (By.CSS_SELECTOR, '#home-content-wrap > div:nth-child(4) > div:nth-child(1) > div > div:nth-child(1) > div')
        # 菜单名：收入证明申请
        self.incomeCertificationMenuLocator = (By.CSS_SELECTOR, '#home-content-wrap > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(1) > div')
        # 菜单名：离职证明申请
        self.leaveCertificateMenuLocator = (By.CSS_SELECTOR, '#home-content-wrap > div:nth-child(4) > div:nth-child(3) > div > div:nth-child(1) > div')
        # 菜单名：其他证明申请
        self.otherCertificateMenuLocator = (By.CSS_SELECTOR, '#home-content-wrap > div:nth-child(4) > div:nth-child(4) > div > div:nth-child(1) > div')

        # 菜单名：证明办理
        self.certificationDealMenuLocator = (By.CSS_SELECTOR,'#home-content-wrap > div:nth-child(10) > div:nth-child(5) > div > div:nth-child(1) > div')
    # 获取‘预入职登记’
    def getPreEntryMenu(self):
        return self.get_element(self.preEntryMenuLocator)
    # 获取‘职位入职二维码’
    def getQrCodeMenu(self):
        return self.get_element(self.qrCodeMenuLocator)
    # 获取‘员工离职共享’
    def getEmployeeTurnOverMenu(self):
        return self.get_element(self.employeeTurnOverMenuLocator)
    # 获取’预入职档案审核‘--二级菜单
    def getFileReviewMenu(self):
        return self.get_element(self.fileReviewMenuLocator)
    # 获取‘入职办理’--二级菜单
    def getEmployeeHiredMenu(self):
        return self.get_element(self.employeeHiredMenuLocator)

    # 获取‘在职证明’--二级菜单
    def getOnJobCertificationMenu(self):
        return self.get_element(self.onJobCertificationMenuLocator)
    # 获取‘收入证明’--二级菜单
    def getIncomeCertificationMenu(self):
        return self.get_element(self.incomeCertificationMenuLocator)
    # 获取‘离职证明’--二级菜单
    def getLeaveCertificateMenu(self):
        return self.get_element(self.leaveCertificateMenuLocator)
    # 获取‘其他证明’--二级菜单
    def getOtherCertificateMenu(self):
        return self.get_element(self.otherCertificateMenuLocator)
