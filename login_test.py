from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://pypi.org/")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
driver.implicitly_wait(5)
