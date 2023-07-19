# -*- coding: utf-8 -*-
# @project:111
# @author:kingdee
# @file:myDriver
# @ide:PyCharm
# @time:2020/9/14  19:02

from selenium import webdriver
from time import sleep
from utils.mySetting import url_94, driverPath,url_30


# 打开浏览器的时候就登录一次
# 在逻辑上可以独立，并且会被重复使用的东西 都可以写在工具类中
class Driver:
    '''浏览器驱动工具类'''
    # 第一次获取时，浏览器驱动对象为空
    # 类成员
    _driver = None  # 习惯加一个下划线 代表这个变量会被子类继承过去使用，没有实际意义

    @classmethod  # 类方法的作用是，可以不用实例化对象，用类名直接调用
    def get_driver(cls, brower_name='Chrome'):
        '''
        获取浏览器驱动对象
        :param brower_name:
        :return:
        '''
        # global driver   # driver是全局对象，需要声明下

        if cls._driver is None:

            if brower_name == 'Chrome':
                cls._driver = webdriver.Chrome(driverPath['Chrome'])
            else:
                cls._driver = webdriver.Firefox(driverPath['Firefox'])
            # 省略别的浏览器

            # 最大化窗口
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)
            # 访问默认登录页面
            # cls._driver.get(url_94)
            cls._driver.get(url_30)
            # 登录
            cls._login()

        return cls._driver

    @classmethod  # 再测试系统时，登录只需要做一次就行，所以可以写在driver类中,只在打开浏览器的时候登录一次
    def _login(cls):
        '''
        类方法，并且是私有的，只能在类里面调用，子类不能继承
        :return:
        '''
        cls._driver.find_element_by_id('username').send_keys('yuandan_chen')
        cls._driver.find_element_by_id('password').send_keys('111')
        cls._driver.find_element_by_id('loginSubmit').click()
        button = cls._driver.find_elements_by_id('btnIgnore')
        if button:
            button[0].click()

        # 手动登录获取到的cookie信息
        # cookieSli = [{'domain': '172.18.7.111', 'httpOnly': False, 'name': 'NAPRoutID', 'path': '/', 'secure': False, 'value': '0'},
        #             {'domain': '172.18.7.111', 'httpOnly': False, 'name': 'EASSESSIONID', 'path': '/', 'secure': False, 'value': '1518176755'},
        #             {'domain': '172.18.7.111', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'rBIHbxrqX5qcPyhd8BmwiEl4g5aMRy2x80IA'},
        #             {'domain': '172.18.7.111', 'httpOnly': False, 'name': 'flag', 'path': '/eassso', 'secure': False, 'value': 'true'},
        #             {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasAuthPattern', 'path': '/eassso', 'secure': False, 'value': 'BaseDB'},
        #              {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasPortalDBType', 'path': '/eassso', 'secure': False, 'value': '3'},
        #              {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasPortalDataCenterCode', 'path': '/eassso', 'secure': False, 'value': 'sql860new_0901'},
        #              {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasPortalUsername', 'path': '/eassso', 'secure': False, 'value': 'yuandan_chen'},
        #              {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasPortalUserId', 'path': '/eassso', 'secure': False, 'value': 'aLfAQUPiT7ezTAdtgLI4dRO33n8%3D'},
        #              {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasPortalDataCenter', 'path': '/eassso', 'secure': False, 'value': '0'},
        #              {'domain': '172.18.7.111', 'expiry': 4105094400, 'httpOnly': False, 'name': 'EasPortalLocale', 'path': '/eassso', 'secure': False, 'value': '0'}]
        # 清除所有的cookie
        # cls._driver.delete_all_cookies()
        #
        # # 将手动登录的cookie添加进去，然后刷新页面
        # for cookie in cookieSli:
        #     cls._driver.add_cookie(cookie)
        #
        # sleep(3)
        #
        # cls._driver.refresh()

        # after_cookie = cls._driver.get_cookies()
        # for i in after_cookie:
        #     print(i)

if __name__ == '__main__':
    Driver.get_driver()  # 类方法不用实例化，直接类名.方法名 调用
