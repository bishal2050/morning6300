import time
import unittest
from POM.Utilities.exceltestcase import Utils
from POM.Locators.driversonly import drivers
from POM.pages.loginpage import login
from ddt import ddt,data, unpack

@ddt
class MyTestCase(unittest.TestCase):



    def setUp(self):
        dr = drivers()
        self.driver = dr.driver
        self.driver.get(dr.url)
        self.driver.maximize_window()
    @data(*Utils.read_data_from_excel("D:\\PythonCourse\\morning6300\\POM\\testdata\\Username_data.xlsx", "Sheet1"))
    @unpack
    def test_login(self, times, new):
        lp = login(self.driver)
        lp.loginpage(times,new)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
