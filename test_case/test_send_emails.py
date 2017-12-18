#coding = utf-8
from selenium import webdriver
import unittest,time
from public import login

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url= "http://www.126.com/"
        self.verificationErrors = []


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


    def test_send_emails(self):
        driver = self.driver
        driver.get(self.base_url)
        #登录
        login.login(self,"tzjjd527","tmjd527527")
        #写信
        driver.find_element_by_css_selector(".nui-ico.fn-bg.ga0").click()
        #收件人
        driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("15156214261@163.com")

        #发送还是有问题
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//*[@class='nui-msgbox-ft-btns']/div/span").click()
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text,u'发送成功')
        login.logout(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
