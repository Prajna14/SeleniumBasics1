from selenium import webdriver
drivers=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/9-3-2019/drivers/chromedriver.exe")
drivers.get("file:///C:/Users/prajn/OneDrive/Desktop/cricketWebTable.html.html")
drivers.maximize_window()
val=drivers.find_elements_by_xpath("//*[@id='cric']/tbody/tr[1]") and drivers.find_elements_by_xpath("//*[@id='cric']/tbody/tr[3]")

print(len(val))
for i in val:
    print((i.text))
