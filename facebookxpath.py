from selenium import webdriver
qspiders=webdriver.Chrome(executable_path="C:\\Users\\prajn\\Downloads\\chromedriver_win32\\chromedriver.exe")
qspiders.get("https://www.facebook.com/")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
# qspiders.find_element_by_id("email").send_keys("prajnakornaya14@gmail.com")
# qspiders.find_element_by_id("pass").send_keys("padmakshih.m29")
# qspiders.find_element_by_id("u_0_2").click()
qspiders.find_element_by_xpath("//input[@name='firstname']").send_keys("abc")
qspiders.find_element_by_xpath("//input[@name='lastname']").send_keys("def")
qspiders.find_element_by_xpath("//input[@aria-label='Mobile number or email address']").send_keys("1234567890")
qspiders.find_element_by_xpath("//input[@aria-label='New password']").send_keys("1234567yzx")
qspiders.find_element_by_xpath("//select[@name='birthday_day']").send_keys("14")
qspiders.find_element_by_xpath("//select[@name='birthday_month']").send_keys("12")
qspiders.find_element_by_xpath("//select[@name='birthday_year']").send_keys("1992")
qspiders.find_element_by_xpath("//input[@value='1']").click()
qspiders.find_element_by_xpath("//button[@name='websubmit']").click()
