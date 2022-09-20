from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://demoblaze.com')
