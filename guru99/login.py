import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.guru99.com/v4/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "uid").send_keys("mngr410077")
driver.find_element(By.NAME, "password").send_keys("YvYhAjU")
driver.find_element(By.NAME, "btnLogin").click()
driver.find_element(By.LINK_TEXT, "New Customer").click()

driver.find_element(By.NAME, "name").send_keys("jashu")
driver.find_element(By.XPATH, "//input[2]").click()
driver.find_element_by_id("dob").click()
driver.find_element_by_id("dob").clear()
driver.find_element_by_id("dob").send_keys("1995")
driver.find_element_by_name("addr").send_keys("Tirupathi")
driver.find_element_by_name("city").send_keys("Tirupathi")
driver.find_element_by_name("state").send_keys("AP")
driver.find_element_by_name("pinno").send_keys("517501")
driver.find_element_by_name("telephoneno").send_keys("9490567040")
driver.find_element_by_name("emailid").send_keys("jagadeeshdeepu@gmail.com")
driver.find_element_by_name("password").send_keys("jaga123")
driver.find_element_by_name("sub").click()
driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::td[1]").click()
driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::a[1]").click()
print("Test completed")
time.sleep(5)
driver.quit()
driver.close()

