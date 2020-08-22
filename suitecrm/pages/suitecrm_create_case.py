from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from selenium.webdriver.common.by import By

from random import randint
import json
import os
from dotenv import load_dotenv


class CreateCases(SuitecrmBasePage):

    CASES = ''
    BUTTON_CASE = (By.LINK_TEXT, 'SOPORTE')
    CASE = (By.LINK_TEXT, 'Casos')
    CREATE_CASE = (By.LINK_TEXT, 'Nuevo Caso')
    TYPE = (By.ID, 'type')
    NAME_ACCOUNT = (By.ID, 'btn_account_name')
    SEARCH_FOR = (By.ID, 'name_advanced')
    SUBJECT = (By.ID, 'name')
    BODY = (By.XPATH, '//*[@id="tinymce"]')
    BODY_RESOL = (By.ID, 'resolution')
    USER_NAME = (By.ID, 'btn_assigned_user_name')
    SEARCH_USER_NAME = (By.ID, 'first_name_advanced')
    SAVE = (By.ID, 'SAVE')
    IFRAME = (By.ID, 'description_ifr')

    VIEW_CASES = (By.LINK_TEXT, 'Ver Casos')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[4]//a'

    CUSTOMER = ''
    USER_FIRST_NAME = ''
    USER_LAST_NAME = ''

    def load_variables(self):

        load_dotenv(os.getcwd() + "/tests/.env")
        self.CUSTOMER = os.getenv("CUSTOMER")
        self.USER_FIRST_NAME = os.getenv("USER_FIRST_NAME")
        self.USER_LAST_NAME = os.getenv("USER_LAST_NAME")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

        with open(os.getcwd() + "/data/data_case.json") as file:
            self.CASES = json.load(file)

        self.TYPE_CASE = self.CASES['type']
        self.TITLE = self.CASES['subject'] + '-' + str(randint(1000, 2000))
        self.DESCRIPTION = self.CASES['description']
        self.RESOLUTION = self.CASES['resolution']

    def access_case(self):

        self.menu_select_option(self.BUTTON_CASE, self.CASE)

    def new_case(self):

        self.wait_button_clickable(self.CREATE_CASE)

        self.click_button(self.CREATE_CASE)

        self.wait_button_clickable(self.TYPE)

        self.fill_select_field(self.TYPE, self.TYPE_CASE)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.NAME_ACCOUNT
        find_data_page.selector_search_field = self.SEARCH_FOR
        find_data_page.search_query = self.CUSTOMER
        find_data_page.open_site_search()

        self.wait_button_clickable(self.SUBJECT)

        self.fill_text_field(self.SUBJECT, self.TITLE)

        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME))

        self.fill_text_field(self.BODY, self.DESCRIPTION)

        self.driver.switch_to.default_content()

        self.fill_text_field(self.BODY_RESOL, self.RESOLUTION)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.USER_NAME
        find_data_page.selector_search_field = self.SEARCH_USER_NAME
        find_data_page.search_query = self.USER_FIRST_NAME
        find_data_page.open_site_search()

        self.send_enter_key(self.SAVE)

        return self.TITLE

    def search_case(self, title):

        user = SuitecrmSiteSearchElement(self.driver)
        user.access_menu = self.VIEW_CASES
        user.press_filter = self.FILTER
        user.table_rows = self.TABLE_ROWS_SELECTOR
        user.name_selector = self.NAME_SELECTOR
        user.col_selector = self.COL_SELECTOR
        value = user.search_element(title)

        return value






