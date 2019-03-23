import time

from selenium import webdriver
import pytest
from framework2.pages.loginpage import LoginPage
from framework2.pages.homepage import Logout_data
from framework2.testdata.data import *


@pytest.fixture('session')
def test_launch_browser():
    global drivers
    drivers = webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/framework2/drivers/chromedriver.exe")
    drivers.get(URL)
    drivers.maximize_window()
    drivers.implicitly_wait(30)


def test_login(test_launch_browser):
    lp = LoginPage(drivers)
    lp.enter_un()  # reusable component
    lp.enter_pwd()  # reusable component
    lp.enter_submit()  # reusable component
    # drivers.find_element_by_id("j_username").send_keys("admin")
    # drivers.find_element_by_name("j_password").send_keys("manager")
    # drivers.find_element_by_name("Submit").click()


def test_logout(test_launch_browser):
    time.sleep(5)
    lp1 = Logout_data(drivers)
    lp1.logout_data()
    # drivers.find_element_by_xpath("//*[text()='log out']").click()
