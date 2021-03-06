from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from lib.suitecrm_base_page import SuitecrmBasePage
from dotenv import load_dotenv
import os


class LoginPage(SuitecrmBasePage):

    USER_NAME = (By.ID, 'user_name')
    USER_PDW = (By.ID, 'username_password')
    BUTTON_SIGN_IN = (By.ID, 'bigbutton')
    USERNAME = ''
    USERNAME_PWD = ''

    def __init__(self, driver):

        super().__init__(driver)
        self.load_variables()

    def load_variables(self):

        load_dotenv(os.getcwd() + "/tests/.env")
        self.USERNAME = os.getenv("USERNAME")
        self.USERNAME_PWD = os.getenv("USERNAME_PWD")

    def login_user(self):

        user = self.driver.find_element(*self.USER_NAME)
        user.click()
        user.send_keys(self.USERNAME)

        pwd = self.driver.find_element(*self.USER_PDW)
        pwd.click()
        pwd.send_keys(self.USERNAME_PWD)

        button_init = self.driver.find_element(*self.BUTTON_SIGN_IN)
        button_init.send_keys(Keys.ENTER)






