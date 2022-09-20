import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service('C:\\Selenium\\chromedriver.exe'))
time.sleep(5)
driver.get("https://www.google.com")
driver.maximize_window()

SearchBar = driver.find_element(By.NAME, "q")
SearchBar.send_keys("broadway"+Keys.ENTER)

# Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
