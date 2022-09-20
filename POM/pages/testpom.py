from POM.Locators.locators_place import locatorscode
from selenium import webdriver

class testpart:
    def testwork(self):
        lc = locatorscode()
        driver = webdriver.Chrome(lc.path)
        driver.get(lc.url)