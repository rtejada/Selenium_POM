import unittest
import HtmlTestRunner
from ddt import ddt, file_data
from selenium import webdriver
import os
from page_objects.login_page import LoginPage



@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        cls.login_page = LoginPage(driver=cls.driver)

    @file_data(os.path.join('data', 'test_login.json'))
    def test_login(self, username, password):
        self.login_page.login_in_app(username=username, password=password)
        is_login_successful = self.login_page.is_login_successful()

        # Assertions
        assert is_login_successful is True

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/home/roxana/Documentos/Selenium_POM/Tutorial_selenium_POM/reports"))
