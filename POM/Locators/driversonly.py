from selenium import webdriver
from POM.Locators.locators_place import locatorscode

class drivers:

    driver = webdriver.Chrome(locatorscode().path)
    url = locatorscode().url
