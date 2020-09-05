class LoginPage:

    # Locators
    USERNAME_INPUT = "txtUsername"
    PASSWORD_INPUT = "txtPassword"
    LOGIN_BTN = "btnLogin"
    WELCOME_USER_LABEL = "welcome"

    def __init__(self, driver):
        self.driver = driver

    # Acciones

    def login_in_app(self, username, password):
        username_input = self.driver.find_element_by_id(self.USERNAME_INPUT)
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_id(self.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_id(self.LOGIN_BTN)
        login_btn.click()

    def is_login_successful(self):
        welcome_user_label = self.driver.find_element_by_id(self.WELCOME_USER_LABEL).is_displayed()
        return welcome_user_label





