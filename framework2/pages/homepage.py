class Logout_data:
    def __init__(self, drivers):
        self.driver = drivers
        self.logout = "//*[@id='header']/div[2]/span/a[2]/b"

    def logout_data(self):
        self.driver.find_element_by_xpath(self.logout).click()

