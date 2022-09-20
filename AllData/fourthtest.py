from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service('C:\Selenium\chromedriver.exe'))
# driver.maximize_window() #it will maximize the browser window
# driver.get("https://demoblaze.com")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://google.com")
