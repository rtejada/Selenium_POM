from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_add_file import SuitecrmAdd
from selenium.webdriver.common.by import By
import json


class FillUserProfile(SuitecrmBasePage):

    USERS = ''
    USER_MANAGEMENT = (By.ID, 'user_management')
    CREATE_NEW_USER = (By.LINK_TEXT, 'Crear Nuevo Usuario')
    USER_NAME = (By.ID, 'user_name')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    STATUS = (By.ID, 'status')
    USER_TYPE = (By.ID, 'UserType')
    SELECT_FILE = (By.ID, 'photo_file')
    FACTOR_AUTH = (By.ID, 'factor_auth')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_users.json") as file:
            self.USERS = json.load(file)

    def fill(self):

        self.click_button(self.USER_MANAGEMENT)

        self.wait_button_clickable(self.CREATE_NEW_USER)

        self.click_button(self.CREATE_NEW_USER)

        self.wait_selector_visible(self.USER_NAME)

        self.fill_text_field(self.USER_NAME, self.USERS['user_name'])

        self.fill_text_field(self.FIRST_NAME, self.USERS['first_name'])

        self.fill_text_field(self.LAST_NAME, self.USERS['last_name'])

        self.fill_select_field(self.STATUS, self.USERS['Employee_Status'])

        self.fill_select_by_text(self.USER_TYPE, self.USERS['Type_User'])

        add_object = SuitecrmAdd(self.driver)
        add_object.select_file = self.SELECT_FILE
        add_object.file_name = 'comercial.png'
        add_object.add_files()

        self.click_button(self.FACTOR_AUTH)


