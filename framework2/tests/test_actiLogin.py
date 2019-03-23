import time

from selenium import webdriver
import pytest

@pytest.fixture('session')
def test_launch_browser():
    global drivers
    drivers=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/framework2/drivers/chromedriver.exe")
    drivers.get("http://localhost:8080/login?from=%2F")
    drivers.maximize_window()
    drivers.implicitly_wait(30)

def test_login(test_launch_browser):
    drivers.find_element_by_id("j_username").send_keys("admin")
    drivers.find_element_by_name("j_password").send_keys("manager")
    drivers.find_element_by_name("Submit").click()

def test_logout(test_launch_browser):
    time.sleep(5)
    drivers.find_element_by_xpath("//*[text()='log out']").click()