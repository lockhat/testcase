#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月8日

@author: BG246077
'''
import unittest,time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from public import login
import HTMLTestRunner
from time import strftime






class TestLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(50)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


    def test_login(self):
        u'''登录名和密码正确时正确登录（登录名为tzjjd527）'''
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        
        login.login(self,"tzjjd527", "tmjd527527")
        text = driver.find_element_by_id("spnUid").text
        self.assertEqual(text, u"tzjjd527@126.com")
        driver.implicitly_wait(3000)
        login.logout(self)
      
    def test_login_1(self):    
        u'''登录名格式错误（登录名为空格）'''
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        
        login.login(self," ", "tmjd527527")
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        self.assertEqual(text, u"帐号格式错误")
        driver.implicitly_wait(3000)
        
    def test_login_2(self):    
        u'''登录名为空'''
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        
        login.login(self,"", "tmjd527527")
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        self.assertEqual(text, u"请输入帐号" )
        driver.implicitly_wait(3000)
      
    def test_login_3(self):    
        u'''密码错误,哈哈哈'''
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        
        login.login(self,"tzjjd527", "tmjd")
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        self.assertEqual(text, u"帐号或密码错误")
        driver.implicitly_wait(3000)
                

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main(verbosity = 2)
    testunit  = unittest.TestSuite()
    testunit.addTest(TestLogin("test_login"))
    testunit.addTest(TestLogin("test_login_1"))
    testunit.addTest(TestLogin("test_login_2"))
    testunit.addTest(TestLogin("test_login_3"))
    now = strftime("%Y-%m-%d %H-%M_%S")
    filename = 'C:\\Users\\Bg246077\\Documents\\LiClipse Workspace\\testcase\\report\\'+now+'result.html'
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"126邮箱登录测试",
        description = u"用例执行情况")
    runner.run(testunit)
    fp.close()