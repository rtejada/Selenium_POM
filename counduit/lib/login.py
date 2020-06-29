from selenium.webdriver.common.by import By
from pages.realworld_base_page import RealworldCounduitBasePage
import os


class Login(RealworldCounduitBasePage):

    LOGIN = ''
    PASS = ''
    INIT_SESSION = 'Sign in'
    BUTTON_MAIL_LOCATOR = (By.XPATH, '//input[@type="email"]')
    BUTTON_PASS_LOCATOR = (By.XPATH, '//input[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')

    def load_variables(self):
        self.LOGIN = os.getenv("LOGIN")
        self.PASS = os.getenv("PASS")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

    def login_user(self):
        sign_up = self.driver.find_element_by_link_text(self.INIT_SESSION)
        sign_up.click()

        email = self.driver.find_element(*self.BUTTON_MAIL_LOCATOR)
        email.click()
        email.send_keys(self.LOGIN)

        password = self.driver.find_element(*self.BUTTON_PASS_LOCATOR)
        password.click()
        password.send_keys(self.PASS)

        sign_in = self.driver.find_element(*self.BUTTON_SUBMIT)
        sign_in.click()
        return self.driver.current_url

