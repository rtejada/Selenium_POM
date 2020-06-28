from selenium.webdriver.common.by import By


class Login:
    INIT_SESSION = 'Sign in'
    LOGIN = 'maripuri@gmail.com'
    PASSW = 'maripuri2020'
    BUTTON_MAIL_LOCATOR = (By.XPATH, '//input[@type="email"]')
    BUTTON_PASS_LOCATOR = (By.XPATH, '//input[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
            self.driver = driver

    def login_user(self):
        sign_up = self.driver.find_element_by_link_text(self.INIT_SESSION)
        sign_up.click()

        email = self.driver.find_element(*self.BUTTON_MAIL_LOCATOR)
        email.click()
        email.send_keys(self.LOGIN)

        password = self.driver.find_element(*self.BUTTON_PASS_LOCATOR)
        password.click()
        password.send_keys(self.PASSW)

        sign_in = self.driver.find_element(*self.BUTTON_SUBMIT)
        sign_in.click()
        return self.driver.current_url

