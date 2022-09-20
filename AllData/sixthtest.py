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
actions = webdriver.ActionChains(driver)

actions.key_down(Keys.SHIFT).send_keys_to_element(SearchBar,"qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()