# -*- coding: utf-8 -*-
# @project:111
# @author:
# @file:1、basePage.py
# @ide:PyCharm
# @time:2020/7/9  19:31
'''basePage模块的功能在于：将各个页面类中相同的操作可以抽离出来'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.myDriver import Driver
from utils.mySetting import url_94,TIMEOUT,POLL_FREQUERY,driverPath,url_30


from selenium.webdriver.common.by import By

class BasePage:
    # 初始化
    def __init__(self):
        self.driver = Driver.get_driver()

    # 析构方法
    def __del__(self):
        """
        析构方法, 对象被销毁时自动执行
        :return:
        """
        self.driver.quit()

    # 获取单个元素
    def get_element(self,locator):
        '''
        (显式等待)根据表达式匹配单个元素，并返回元素对象
        :param locator:是一个元组，第0个元素表示定位方法，第一个元素表示元素定位表达式
        :return:
        '''
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 传入轮询时间
            poll_frequency=POLL_FREQUERY
        ).until(
            EC.visibility_of_element_located(locator)
        )

        # 返回元素对象
        return self.driver.find_element(*locator)

    # 获取元素列表
    def get_elements(self, locator):
        '''
        (显式等待)根据表达式匹配单个元素，并返回元素对象
        :param locator:是一个元组，第0个元素表示定位方法，第一个元素表示元素定位表达式
        :return:
        '''
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 传入轮询时间
            poll_frequency=POLL_FREQUERY
        ).until(
            EC.visibility_of_element_located(locator)
        )

        # 返回元素对象
        return self.driver.find_elements(*locator)


if __name__ == "__main__":
    BasePage().get_element((By.ID,'#username'))




