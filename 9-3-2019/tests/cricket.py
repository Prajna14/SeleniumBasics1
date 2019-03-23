from selenium import webdriver
drivers=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/9-3-2019/drivers/chromedriver.exe")
drivers.get("file:///C:/Users/prajn/OneDrive/Desktop/cricketWebTable.html.html")
drivers.maximize_window()
#drivers.implicitly_wait(30)
# val=drivers.find_element_by_xpath("//*[@id='cric']/tbody/tr[3]/td[1]").text
val=drivers.find_element_by_xpath("//*[@id='cric']/tbody/tr[3]/td[1]")
print(type(val))
#print((val.text))
print(type(val.text))
val1=drivers.find_elements_by_xpath("//*[@id='cric']/tbody/tr/td")
# print(type(val1))
# print((val1.text))
print(len(val1))
for i in val1:
    print((i.text))
