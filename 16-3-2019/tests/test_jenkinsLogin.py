from selenium import webdriver
import time
from qsp.pages.loginpage import LoginPage1


def test_launch_browser():
    global drivers
    drivers=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/16-3-2019/drivers/chromedriver.exe")
    drivers.get("http://localhost:8080/login?from=%2F")
    drivers.maximize_window()
    drivers.implicitly_wait(30)
def test_login():
    # drivers.find_element_by_id("j_username").send_keys("admin")
    # drivers.find_element_by_name("j_password").send_keys("manager")
    lp=LoginPage1(drivers)
    lp.enter_un()
    lp.enter_pwd()
    drivers.find_element_by_name("Submit").click()

def test_logout():
    time.sleep(5)
    drivers.find_element_by_xpath("//*[text()='log out']").click()