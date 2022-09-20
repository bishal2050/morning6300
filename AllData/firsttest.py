#we will import selenium as well as webdriver
from selenium import webdriver
#here we defined a variable named driver with the location of webdriver
driver = webdriver.Chrome('C:\Selenium\chromedriver.exe')
driver.maximize_window() #it will maximize the browser window
driver.get("https://demoblaze.com")
driver.quit()
'''If we are closing the whole window or browser we will choose quit because it will kill session also
But if we are closing only the tab that has been opened we choose close'''


