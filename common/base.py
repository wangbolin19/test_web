"""
封装打开浏览器(方法)
    def open_browser()
建立Base类
class Base:
    1.输入网址
    2.元素定位
    3.元素操作

base.py文件是可以复用,适用于任何项目中
"""
import time

from selenium import webdriver
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_browser(brower='chrome'):

    if brower == "chrome":
        driver = webdriver.Chrome()

    elif brower  == "firefox":
        driver = webdriver.Firefox()

    elif brower == "ie":
        driver = webdriver.Ie()
    else:
        driver = None
        print("请选择正确的浏览器,例如:'chrome','firefox','ie'")

    return driver

class Base():

    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        """
        打开网址
        :param url:  被测的网站
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()  # 窗口最大化

    def find_element(self,locator,timeout=10):
        """
        定位一个元素 返回单个元素
        :param locator:  定位器,元组
        :param timeout:  最大等待时间
        :return:
        """
        element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator,timeout=10):
        """
        定位一组元素 返回元素列表
        :param locator:
        :param timeout:
        :return:
        """
        elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements
    def click(self,locator,timeout=10):  # 点击元素

        element = self.find_element(locator,timeout)
        element.click()

    def send_keys(self,locator,text,timeout=10):  # 元素输入
        element = self.find_element(locator,timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,locator,text,timeout=10):
        """
        判断文本是否存在于元素中, 相等返回True,不相等返回False
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False
    def is_value_in_element(self,locator,value,timeout=10):
        """
        判断元素的value属性是否与value是否相等,如果相等返回True,不相等返回False
        :param locator:
        :param value:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()



if __name__ == '__main__':
    driver = open_browser()
    base = Base(driver)
    url = "http://ecshop.itsoso.cn"
    base.open_url(url)
    locator_a = ("link text","请登录")
    base.click(locator_a)
    locator = ("name","username")
    base.send_keys(locator,text="admin")
    locator1 = ("name","password")
    base.send_keys(locator1,text="123456")

    time.sleep(5)
    driver.quit()
