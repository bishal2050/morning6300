from selenium.webdriver.common.by import By
from POM.Locators.locators_place import locatorscode
class login:

    def __init__(self,driver):
        self.lc = locatorscode()
        self.driver = driver

    def loginpage(self,username,password):
        lc = self.lc
        driver = self.driver
        driver.find_element(By.ID,lc.login_link).click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, lc.textbox_username).send_keys(username)
        driver.find_element(By.XPATH, lc.textbox_password).send_keys(password)
        driver.find_element(By.XPATH, lc.login_submit).click()