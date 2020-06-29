from pages.suitecrm_base_page import SuitecrmBasePage
import os


class AuthBasicPage(SuitecrmBasePage):
    USER = ''
    PWD = ''
    URL_AUTH_BASIC = ''

    def load_variables(self):

        self.USER = os.getenv("AUTH_BASIC_USER")
        self.PWD = os.getenv("AUTH_BASIC_PWD")
        self.URL_AUTH_BASIC = os.getenv("URL_AUTH_BASIC")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

    def authenticate(self):

        self.driver.get(self.URL_AUTH_BASIC.format(self.USER, self.PWD))
