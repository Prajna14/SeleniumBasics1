from selenium import webdriver
qspiders = webdriver.Firefox(executable_path="C:\\Users\\prajn\\Downloads\\geckodriver-v0.24.0-win64\\geckodriver.exe")
qspiders.get("http://google.com")