from selenium import webdriver
drivers=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/9-3-2019/drivers/chromedriver.exe")
drivers.get("file:///C:/Users/prajn/OneDrive/Desktop/loginData.html")
drivers.maximize_window()
#drivers.implicitly_wait(30)
drivers.find_element_by_id("un").send_keys('BTM')
#drivers.find_element_by_id("unwdws").send_keys('BTM')
drivers.find_element_by_id("pwd").send_keys('QSPIDERS')
drivers.find_element_by_id("login").click()

val=drivers.find_element_by_id("pwd").get_attribute('type')
print(val)
text=drivers.find_element_by_id("login").text
print(text)
val1=drivers.find_element_by_id("un").text
print(val1)
