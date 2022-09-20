from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service('C:\\Selenium\\chromedriver.exe'))
driver.maximize_window()
driver.get("https://demoblaze.com")
Login = driver.find_element(By.ID, 'login2')
Login.click()
username = ww(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginusername"]')))
username.send_keys('testmorning')
password = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
password.send_keys('test123')
submit = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
submit.click()