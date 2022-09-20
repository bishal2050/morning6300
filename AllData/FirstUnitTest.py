import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service('C:\\Selenium\\chromedriver.exe'))
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com")

    def test_one(self):
        driver = self.driver
        Login = driver.find_element(By.ID, 'login2')
        Login.click()
        username = ww(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginusername"]')))
        username.send_keys('testmorning')
        password = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
        password.send_keys('test123')
        submit = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        submit.click()
        result = "Welcome testmorning"
        value = ww(driver,10).until(EC.visibility_of_element_located((By.ID, 'nameofuser'))).text
        self.assertEqual(result,value,"Doesnot match")



    def tearDown(self) -> None:
        self.driver.quit()




if __name__=='main':
    unittest.main()
