from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from lib.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By
import json
from random import randint


class CreateCall(SuitecrmBasePage):
    LIST_INVITEES = ['invitees_add_2', 'invitees_add_3', 'invitees_add_4', 'invitees_add_5']
    HOUR_MIN = [11, 30, 1]
    CALL_DATA = ''
    CALL_NAME = ''
    BUTTON_ALL = (By.LINK_TEXT, 'TODO')
    CALLED = (By.LINK_TEXT, 'Llamadas')
    REGISTER_CALL = (By.LINK_TEXT, 'Registrar Llamada')
    SUBJECT = (By.ID, 'name')
    START = (By.ID, 'date_start_trigger')
    CALENDAR_START_DAY = (By.XPATH, '//*[@id="date_start_trigger_div_t_cell22"]/a')
    DATE_START_HOURS = (By.ID, 'date_start_hours')
    DATE_START_MINUTES = (By.ID, 'date_start_minutes')
    DURATION_HOURS = (By.ID, 'duration_hours')
    DURATION_MINUTES = (By.ID, 'duration_minutes')
    DESCRIPTION = (By.ID, 'description')

    LINK_CUSTOMER = (By.ID, 'btn_parent_name')
    NAME_ACCOUNT = (By.ID, 'name_advanced')
    ASSIGNED_USER = (By.ID, 'btn_assigned_user_name')
    USER_NAME = (By.ID, 'first_name_advanced')

    SEARCH = (By.ID, 'invitees_search')
    ADD_FIRST_INVITE = (By.ID, 'invitees_add_1')
    CALL_SAVE = (By.NAME, 'button')

    VIEW_CALLED = (By.LINK_TEXT, 'Ver Llamadas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[5]//a'

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_users.json") as file:
            self.CALL_DATA = json.load(file)

        self.CALL_SUBJECT = self.CALL_DATA['subject'] + str(randint(8000, 10000))
        self.CUSTOMER = self.CALL_DATA['customer_name']
        self.CALL_DESCRIPTION = self.CALL_DATA['description']
        self.USER = self.CALL_DATA['name_assistance']

    def log_call(self):

        self.menu_select_option(self.BUTTON_ALL, self.CALLED)

        self.wait_button_clickable(self.REGISTER_CALL)

        self.click_button(self.REGISTER_CALL)

        self.wait_button_clickable(self.SUBJECT)

        self.fill_text_field(self.SUBJECT, self.CALL_SUBJECT)

        self.click_button(self.START)

        self.wait_button_clickable(self.CALENDAR_START_DAY)

        self.click_button(self.CALENDAR_START_DAY)

        self.fill_select_field(self.DATE_START_HOURS, str(self.HOUR_MIN[0]))

        self.fill_select_field(self.DATE_START_MINUTES, str(self.HOUR_MIN[1]))

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.LINK_CUSTOMER
        find_data_page.selector_search_field = self.NAME_ACCOUNT
        find_data_page.search_query = self.CUSTOMER
        find_data_page.open_site_search()

        self.fill_text_field(self.DURATION_HOURS, str(self.HOUR_MIN[2]))

        self.fill_select_field(self.DATE_START_MINUTES, str(self.HOUR_MIN[1]))

        self.fill_text_field(self.DESCRIPTION, self.CALL_DESCRIPTION)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.ASSIGNED_USER
        find_data_page.selector_search_field = self.USER_NAME
        find_data_page.search_query = self.USER
        find_data_page.open_site_search()

        self.click_button(self.SEARCH)

        self.wait_button_clickable(self.ADD_FIRST_INVITE)

        self.window_scroll_half()

        for invites in self.LIST_INVITEES:
            self.CALL_NAME = (By.ID, invites)
            self.click_button(self.CALL_NAME)

        self.window_scroll_home()

        self.send_enter_key(self.CALL_SAVE)

    def get_call(self):
        return self.CALL_SUBJECT

    def search_call(self, subject_meeting):
        search_meeting = SuitecrmSiteSearchElement(self.driver)
        search_meeting.access_option = self.VIEW_CALLED
        search_meeting.press_filter = self.FILTER
        search_meeting.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_meeting.col_selector = self.COL_SELECTOR
        search_meeting.name_selector = self.NAME_SELECTOR
        value = search_meeting.search_element(subject_meeting)

        return value






