import time

from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/chromedriver.exe")
driver.get("https://www.srsbooking.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//span[text()='Contact']").click()
driver.find_element_by_xpath("//span[text()='Print Ticket']").click()
driver.back()
time.sleep(10)
driver.forward()
