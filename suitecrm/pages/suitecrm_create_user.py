from lib.suitecrm_base_page import SuitecrmBasePage
from pages.suitecrm_user_profile import FillUserProfile
from pages.suitecrm_employee_information import FillEmployeeInfo
from lib.suitecrm_search_users import SearchUsers
from selenium.webdriver.common.by import By
import json
from random import randint


class CreateUser(SuitecrmBasePage):

    USERS = ''
    ACCESS_ADMIN = (By.XPATH, '//*[@id="with-label"]/span[2]')
    ADMINISTRATOR = (By.LINK_TEXT, 'Administrador')
    PWD = (By.ID, 'tab2')
    NEW_PASS = (By.ID, 'new_password')
    CONFIRM_PASS = (By.ID, 'confirm_pwd')

    SAVE = (By.ID, 'SAVE_HEADER')

    FULL_NAME = (By.ID, 'full_name')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_users.json") as file:
            self.USERS = json.load(file)

        self.USERS['pass'] = self.USERS['pass'] + str(randint(1000, 2000))

    def select_menu(self):

        self.menu_select_option(self.ACCESS_ADMIN, self.ADMINISTRATOR)

    def fill_user_profile(self):

        user_profile = FillUserProfile(self.driver)
        user_name, complete_name = user_profile.fill()

        return user_name, complete_name

    def fill_employee_info(self):

        employee_info = FillEmployeeInfo(self.driver)
        employee_info.fill()

    def fill_password(self):

        self.window_scroll_home()

        self.click_button(self.PWD)

        self.fill_text_field(self.NEW_PASS, self.USERS['pass'])
        self.fill_text_field(self.CONFIRM_PASS, self.USERS['pass'])

    def save(self):

        self.send_enter_key(self.SAVE)

    def search_user(self, complete_name):

        user = SearchUsers(self.driver)
        user.search_user(complete_name)

        #return username


