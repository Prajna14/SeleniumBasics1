import time

from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users/prajn/PycharmProjects/Selenium/SeleniumBasics/chromedriver.exe")
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(30)
cur_win_id=driver.current_window_handle
# win_id2=driver.window_handles
# print(win_id1)
# print(win_id2)
time.sleep(15)
driver.find_element_by_xpath("//span[text()='Login']").click()
mul_wind_id=driver.window_handles
for id in mul_wind_id:
    if (cur_win_id!=id):
        driver.switch_to.window(id)
        time.sleep(10)
        driver.find_element_by_id("inputEmail").send_keys("abc")
# driver.close()
# time.sleep(3)
driver.quit()

# print(mul_wind_id)
# print(type(mul_wind_id))
# print(mul_wind_id[1])
# driver.switch_to.window(mul_wind_id[1])
