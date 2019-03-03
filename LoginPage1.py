from selenium import webdriver
qspiders=webdriver.Chrome(executable_path="C:\\Users\\prajn\\Downloads\\chromedriver_win32\\chromedriver.exe")
qspiders.get("file:///C:/Users/prajn/OneDrive/Desktop/LoginPage1.html")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
qspiders.find_element_by_id("123").send_keys("admin")
qspiders.find_element_by_id("123").send_keys("manager")
qspiders.find_element_by_id("111").click()
