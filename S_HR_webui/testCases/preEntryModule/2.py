# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:2
# @ide:PyCharm
# @time:2020/11/29  11:13
from selenium import webdriver
import time
# 登录shr系统
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('http://172.18.7.94:6888/eassso/login?service=http%3A%2F%2F172.18.7.94%3A6888%2Fshr%2F')
driver.maximize_window()

driver.find_element_by_id('username').send_keys('yuandan_chen')
driver.find_element_by_id('loginSubmit').click()
driver.find_elements_by_id('btnIgnore')

driver.get('http://172.18.7.94:6888/shr/dynamic.do?uipk=hr.ssc.enrollprocesstaskedit&serviceId=e74AAACcikvyPSkQ&inFrame=true&billId=4i4AAAACzwYz6PLb&jobId=5v1dWKyeQNC%2BPINL0FvD54hFHw0%3D&method=view')

driver.find_element_by_css_selector('#sidebar>div.itembox1 > ol > li:nth-child(1)>span>input').click()
driver.find_element_by_css_selector('#sidebar>div.itembox1 > ol > li:nth-child(2)>span>input').click()
driver.find_element_by_css_selector('#sidebar>div.itembox1 > ol > li:nth-child(3)>span>input').click()
driver.find_element_by_css_selector('#sidebar>div.itembox1 > ol > li:nth-child(4)>span>input').click()
driver.find_element_by_css_selector('#sidebar>div.itembox1 > ol > li:nth-child(5)>span>input').click()
driver.find_element_by_css_selector('#confirm_entry').click()





