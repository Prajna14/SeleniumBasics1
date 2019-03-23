from framework2.testdata.data import *
class LoginPage:
    def __init__(self, drivers):
        self.driver = drivers
        self.un_locator = 'j_username'
        self.pwd_locator = "j_password"
        self.submit = "Submit"

    def enter_un(self):
        self.driver.find_element_by_id(self.un_locator).send_keys(UN)

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_locator).send_keys(PWD)

    def enter_submit(self):
        self.driver.find_element_by_name(self.submit).click()
