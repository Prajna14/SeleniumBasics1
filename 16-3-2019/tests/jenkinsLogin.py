from selenium import webdriver
import time
drivers=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/16-3-2019/drivers/chromedriver.exe")
drivers.get("http://localhost:8080/login?from=%2F")
drivers.maximize_window()
drivers.implicitly_wait(30)
drivers.find_element_by_id("j_username").send_keys("admin")
drivers.find_element_by_name("j_password").send_keys("manager")
drivers.find_element_by_name("Submit").click()

time.sleep(5)
drivers.find_element_by_xpath("//*[text()='log out']").click()