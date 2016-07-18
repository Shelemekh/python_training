# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login_logout(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_login_logout(self):
        success = True
        wd = self.wd
        wd.get("http://oll.tv/")
        wd.find_element_by_id("AuthForm_email").click()
        wd.find_element_by_id("AuthForm_email").send_keys("\\undefined")
        wd.find_element_by_id("AuthForm_password").click()
        wd.find_element_by_id("AuthForm_password").send_keys("\\undefined")
        wd.find_element_by_css_selector("input.b-new-password-input").click()
        wd.find_element_by_css_selector("input.b-new-password-input").send_keys("\\undefined")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("AuthForm_email").click()
        wd.find_element_by_id("AuthForm_email").clear()
        wd.find_element_by_id("AuthForm_email").send_keys("k.shelemekh@digitalscreens.com.ua")
        wd.find_element_by_id("AuthForm_password").click()
        wd.find_element_by_id("AuthForm_password").clear()
        wd.find_element_by_id("AuthForm_password").send_keys("Bokonon_1")
        wd.find_element_by_css_selector("input.btn-yellow.b-submit").click()
        wd.find_element_by_link_text("Выйти").click()
        wd.find_element_by_id("AuthForm_email").click()
        wd.find_element_by_id("AuthForm_email").send_keys("\\undefined")
        wd.find_element_by_id("AuthForm_password").click()
        wd.find_element_by_id("AuthForm_password").send_keys("\\undefined")
        wd.find_element_by_css_selector("input.b-new-password-input").click()
        wd.find_element_by_css_selector("input.b-new-password-input").send_keys("\\undefined")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
