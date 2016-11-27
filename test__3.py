# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://portal.bugfinders.com/6d6002216bdce0ff17d66ea10534ff707a79dcf54cac759d8db85e7761e4e4a7979d19e240ae662811790fce089fb8549f2b6bc6f5674ec7816a1da6df27ab4emwrxnZhqcCClFF5RvXgivVNNOoEZmCSPPjat_2FHj_2BBEI_3D"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_3(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("un").clear()
        driver.find_element_by_id("un").send_keys("boroforit@gmail.com")
        driver.find_element_by_id("pw").clear()
        driver.find_element_by_id("pw").send_keys("aF5JGsjsn5zEqqv")
        driver.find_element_by_css_selector("input.button").click()
        driver.find_element_by_link_text("My Devices").click()
        driver.find_element_by_link_text("Windows 10").click()
        driver.find_element_by_link_text("Account details").click()
        driver.find_element_by_link_text("Functional projects").click()
        driver.find_element_by_link_text("Log out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
