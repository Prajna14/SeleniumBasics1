from selenium import webdriver
qspiders=webdriver.Chrome(executable_path="C:\\Users\\prajn\\Downloads\\chromedriver_win32\\chromedriver.exe")
qspiders.get("https://in.linkedin.com/")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
qspiders.find_element_by_id("reg-firstname").send_keys("abc")
qspiders.find_element_by_id("reg-lastname").send_keys("manager")
qspiders.find_element_by_id("reg-email").send_keys("manager")
qspiders.find_element_by_id("reg-password").send_keys("manager")
qspiders.find_element_by_id("111").click()

