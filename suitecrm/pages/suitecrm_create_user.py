from pages.suitecrm_base_page import SuitecrmBasePage
from pages.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By
import json


class CreateNewUser(SuitecrmBasePage):

    USERS = ''
    ACCESS_ADMIN = (By.XPATH, '//*[@id="with-label"]/span[2]')
    ADMINISTRATOR = (By.LINK_TEXT, 'Administrador')
    USER_MANAGEMENT = (By.ID, 'user_management')
    CREATE_NEW_USER = (By.LINK_TEXT, 'Crear Nuevo Usuario')
    USER_NAME = (By.ID, 'user_name')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    STATUS = (By.ID, 'status')
    USER_TYPE = (By.ID, 'UserType')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_users.json") as file:
            self.USERS = json.load(file)

    def access_administrator(self):

        self.menu_select_option(self.ACCESS_ADMIN, self.ADMINISTRATOR)

    def create_new_user(self):

        self.click_button(self.USER_MANAGEMENT)

        self.wait_button_clickable(self.CREATE_NEW_USER)

        self.click_button(self.CREATE_NEW_USER)

        self.wait_selector_visible(self.USER_NAME)

        self.fill_text_field(self.USER_NAME, self.USERS['user_name'])

        self.fill_text_field(self.FIRST_NAME, self.USERS['first_name'])

        self.fill_text_field(self.LAST_NAME, self.USERS['last_name'])

        self.fill_select_field(self.STATUS, self.USERS['Employee_Status'])

        self.fill_select_by_text(self.USER_TYPE, self.USERS)