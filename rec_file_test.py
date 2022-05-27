# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class Log(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("demo guru99.com/v4")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[1]/following::div[29]").click()
        driver.find_element_by_xpath("//div[@id='rso']/div/div/div/div/a/h3").click()
        # ERROR: Caught exception [unknown command []]
        driver.get("https://demo.guru99.com/v4/")
        driver.find_element_by_name("uid").click()
        driver.find_element_by_name("uid").clear()
        driver.find_element_by_name("uid").send_keys("mngr410077")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("YvYhAjU")
        driver.find_element_by_name("btnLogin").click()
        driver.find_element_by_link_text("New Customer").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("jashu")
        driver.find_element_by_xpath("//input[2]").click()
        driver.find_element_by_id("dob").click()
        driver.find_element_by_id("dob").clear()
        driver.find_element_by_id("dob").send_keys("1995-02-20")
        driver.find_element_by_name("addr").click()
        driver.find_element_by_name("addr").clear()
        driver.find_element_by_name("addr").send_keys("Tirupathi")
        driver.find_element_by_name("city").click()
        driver.find_element_by_name("city").clear()
        driver.find_element_by_name("city").send_keys("Tirupathi")
        driver.find_element_by_name("state").click()
        driver.find_element_by_name("state").clear()
        driver.find_element_by_name("state").send_keys("AP")
        driver.find_element_by_name("pinno").click()
        driver.find_element_by_name("pinno").clear()
        driver.find_element_by_name("pinno").send_keys("517501")
        driver.find_element_by_name("telephoneno").click()
        driver.find_element_by_name("telephoneno").clear()
        driver.find_element_by_name("telephoneno").send_keys("9490567040")
        driver.find_element_by_name("emailid").click()
        driver.find_element_by_name("emailid").clear()
        driver.find_element_by_name("emailid").send_keys("jagadeeshdeepu@gmail.com")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("jaga123")
        driver.find_element_by_name("sub").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::td[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::a[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
