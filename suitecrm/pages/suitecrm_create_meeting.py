from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from selenium.webdriver.common.by import By
from random import randint
import json
import os

class CreateNewMeeting(SuitecrmBasePage):

    LIST_INVITEES = ['invitees_add_1', 'invitees_add_2', 'invitees_add_3', 'invitees_add_4']
    INVITE_NAME = ''
    LIST_MEETING = ''
    BUTTON_ALL = (By.LINK_TEXT, 'TODO')
    MEETING = (By.LINK_TEXT, 'Reuniones')
    SCHEDULE_MEETING = (By.LINK_TEXT, 'Programar Reunión')
    SUBJECT = (By.ID, 'name')
    START = (By.ID, 'date_start_trigger')
    CALENDAR_START_DAY = (By.XPATH, '//*[@id="date_start_trigger_div_t_cell36"]/a')
    NEXT_MONTH = (By.XPATH, '//*[@id="date_end_trigger_div_t"]/thead/tr/th/div/a[3]')
    END = (By.ID, 'date_end_trigger')
    END_DATE = (By.XPATH, '//*[@id="date_end_trigger_div_t_cell29"]/a')

    LINK_CUSTOMER = (By.ID, 'btn_parent_name')
    NAME_ACCOUNT = (By.ID, 'name_advanced')
    ASSIGNED_USER = (By.ID, 'btn_assigned_user_name')
    USER_NAME = (By.ID, 'first_name_advanced')

    LOCATION = (By.ID, 'location')
    DESCRIPTION = (By.ID, 'description')
    PARTICIPANTS = (By.ID, 'search_first_name')
    SEARCH = (By.ID, 'invitees_search')
    ADD_FIRST_INVITE = (By.ID, 'invitees_add_1')
    SAVE_MEETING = (By.NAME, 'button')

    VIEW_MEETING = (By.LINK_TEXT, 'Ver Reuniones')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[4]//a'

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/data/data_users.json") as file:
            self.LIST_MEETING = json.load(file)

        self.SUBJECT_MEETING = self.LIST_MEETING['subject'] + str(randint(500, 1000))
        self.CUSTOMER = self.LIST_MEETING['customer_name']
        self.DESCRIPTION_MEETING = self.LIST_MEETING['description']
        self.LOCAL = self.LIST_MEETING['state_prov_address']
        self.USER = self.LIST_MEETING['name_assistance']

    def create(self):

        self.menu_select_option(self.BUTTON_ALL, self.MEETING)

        self.wait_selector_visible(self.SCHEDULE_MEETING)

        self.click_button(self.SCHEDULE_MEETING)

        self.wait_selector_visible(self.SUBJECT)

        self.fill_text_field(self.SUBJECT, self.SUBJECT_MEETING)

        self.click_button(self.START)

        self.wait_button_clickable(self.CALENDAR_START_DAY)

        self.click_button(self.CALENDAR_START_DAY)

        self.click_button(self.END)

        self.wait_button_clickable(self.END_DATE)

        self.click_button(self.NEXT_MONTH)

        self.click_button(self.END_DATE)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.LINK_CUSTOMER
        find_data_page.selector_search_field = self.NAME_ACCOUNT
        find_data_page.search_query = self.CUSTOMER
        find_data_page.open_site_search()

        self.fill_text_field(self.LOCATION, self.LOCAL)
        self.fill_text_field(self.DESCRIPTION, self.DESCRIPTION_MEETING)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.ASSIGNED_USER
        find_data_page.selector_search_field = self.USER_NAME
        find_data_page.search_query = self.USER
        find_data_page.open_site_search()

        self.click_button(self.SEARCH)

        self.wait_button_clickable(self.ADD_FIRST_INVITE)

        self.window_scroll_half()

        for invites in self.LIST_INVITEES:
            self.INVITE_NAME = (By.ID, invites)
            self.click_button(self.INVITE_NAME)

        self.window_scroll_home()

        self.send_enter_key(self.SAVE_MEETING)
    
    def get_meeting(self):

        return self.SUBJECT_MEETING
    
    def search_meeting(self, subject_meeting):
        search_meeting = SuitecrmSiteSearchElement(self.driver)
        search_meeting.access_option = self.VIEW_MEETING
        search_meeting.press_filter = self.FILTER
        search_meeting.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_meeting.col_selector = self.COL_SELECTOR
        search_meeting.name_selector = self.NAME_SELECTOR
        value = search_meeting.search_element(subject_meeting)

        return value
