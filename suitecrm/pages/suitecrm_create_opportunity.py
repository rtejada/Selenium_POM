from pages.suitecrm_base_page import SuitecrmBasePage
from pages.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By

from random import randint
import json
import os
import time


class CreateNewOpportunity(SuitecrmBasePage):

    OPPORTUNITY = ''
    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_OPPORTUNITY = (By.LINK_TEXT, 'Crear Oportunidades')
    NAME_OPPORTUNITY = (By.ID, 'name')
    WINDOW_VISIBLE = (By. ID, 'date_closed')
    CLOSING_DATE = (By.ID, 'date_closed_trigger')
    DATE = (By.ID, 'date_closed_trigger_div_t_cell22')
    OPPORTUNITY_AMOUNT = (By.ID, 'amount')
    OPPORTUNITY_TYPE = (By.ID, 'opportunity_type')
    SALES_STAGE = (By.ID, 'sales_stage')
    LEAD_SOURCE = (By.ID, 'lead_source')

    SEARCH_ACCOUNT = (By.ID, 'btn_account_name')
    SEARCH_CAMPAIGN = (By.ID, 'btn_campaign_name')
    SEARCH_FOR = (By.ID, 'name_advanced')

    CUSTOMER = ''
    MAIL_CUSTOMER = ''
    TELEPHONE = ''
    WEB = ''
    CAMPAIGN = ''

    def load_variables(self):
        self.CUSTOMER = os.getenv("CUSTOMER")
        self.MAIL_CUSTOMER = os.getenv("MAIL_CUSTOMER")
        self.TELEPHONE = os.getenv("TELEPHONE")
        self.WEB = os.getenv("WEB")
        self.CAMPAIGN = os.getenv("CAMPAIGN")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

        with open("../data/data_opportunity.json") as file:
            self.OPPORTUNITY = json.load(file)

        self.OPPORTUNITY['name_opportunity'] = self.OPPORTUNITY['name_opportunity'] + '-' + str(randint(1000, 2000))
        self.OPPORTUNITY['email'] = str(randint(1000, 2000)) + (self.OPPORTUNITY['email'])

    def access_opportunity(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_OPPORTUNITY)

    def create_new_opportunity(self):

        self.fill_text_field(self.NAME_OPPORTUNITY, self.OPPORTUNITY['name_opportunity'])

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.SEARCH_ACCOUNT
        find_data_page.selector_search_field = self.SEARCH_FOR
        find_data_page.search_query = self.CUSTOMER
        find_data_page.open_site_search()

        self.click_button(self.CLOSING_DATE)

        self.wait_selector_visible(self.DATE)

        self.click_button(self.DATE)

        self.fill_text_field(self.OPPORTUNITY_AMOUNT, self.OPPORTUNITY['amount_opportunity'])

        self.fill_select_field(self.OPPORTUNITY_TYPE, self.OPPORTUNITY['business value'])

        self.fill_select_field(self.SALES_STAGE, self.OPPORTUNITY['default value'])

        self.fill_select_field(self.LEAD_SOURCE, self.OPPORTUNITY['customer_value'])

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.SEARCH_CAMPAIGN
        find_data_page.selector_search_field = self.SEARCH_FOR
        find_data_page.search_query = self.CAMPAIGN
        find_data_page.open_site_search()

        time.sleep(10)






