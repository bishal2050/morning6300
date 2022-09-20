import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = 'C:\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(path))
URL = "https://demo.automationtesting.in/Alerts.html"
driver.get(URL)
driver.maximize_window()
AlertWithOkLink = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
AlertWithOkLink.click()
Button = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
Button.click()
time.sleep(5)
driver.switch_to.alert.accept()

