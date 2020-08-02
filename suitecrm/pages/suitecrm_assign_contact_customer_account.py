from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_customer import SearchCustomer
from lib.suitecrm_site_search import SuitecrmSiteSearch
import json


class AssignContactCustomerAccount(SuitecrmBasePage):

    DATA_USERS = ''
    BUTTON_CONTACT = (By.LINK_TEXT, 'CONTACTOS')
    ADD_CONTACT = (By.LINK_TEXT, 'Seleccionar')
    ACCESS_SELECT = (By.XPATH, '//*[@id="list_subpanel_contacts"]/table//td/table/tbody//li/span')
    LAST_NAME = (By.ID, 'last_name_advanced')
    BUTTON_SEARCH = (By.XPATH, '//*[@id="search_form_submit"]')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_users.json") as file:
            self.DATA_USERS = json.load(file)

        self.CUSTOMER_NAME = self.DATA_USERS['customer_name']
        self.CONTACT_NAME = self.DATA_USERS['contact_name']
        self.CONTACT_LAST_NAME = self.DATA_USERS['contact_last_name']

    def customer_assign_contact(self):
        find_data_customer = SearchCustomer(self.driver)
        find_data_customer.search_customer(self.CUSTOMER_NAME)

        self.window_scroll()

        self.menu_select_option(self.BUTTON_CONTACT, self.ACCESS_SELECT)

        self.wait_selector_visible(self.ADD_CONTACT)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.ADD_CONTACT
        find_data_page.selector_search_field = self.LAST_NAME
        find_data_page.search_query = self.CONTACT_LAST_NAME
        find_data_page.open_site_search()


