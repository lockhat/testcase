#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月8日

@author: BG246077
'''


def login(self,username,password):
        driver = self.driver
        
        
        frame1 = driver.find_element_by_xpath("//iframe[@id='x-URS-iframe']")
        driver.switch_to.frame(frame1)

        driver.find_element_by_xpath("//*[@placeholder='邮箱帐号或手机号']").send_keys(username)
        driver.find_element_by_xpath("//*[@data-placeholder='密码']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='dologin']").click()
        driver.implicitly_wait(3000)
        #time.sleep(20)
        
def logout(self):
        driver = self.driver
        
        driver.find_element_by_link_text(u"退出").click()
        
