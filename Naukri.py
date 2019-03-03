from selenium import webdriver
qspiders=webdriver.Chrome(executable_path="C:\\Users\\prajn\\Downloads\\chromedriver_win32\\chromedriver.exe")
qspiders.get("https://www.facebook.com/")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
qspiders.find_element_by_email("prajnakornaya14@gmail.com").send_keys("admin")
qspiders.find_element_by_name("pwd").send_keys("manager")
qspiders.find_element_by_id("111").click()
