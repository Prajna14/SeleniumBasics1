class LoginPage1:
    def __init__(self,drivers):
        self.driver=drivers
        self.un_locator="j_username"
        self.pwd_locator="j_password"
    def enter_un(self):
        self.driver.find_element_by_id(self.un_locator).send_keys("admin")
    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_locator).send_keys("manager")