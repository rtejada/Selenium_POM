from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
from lib.suitecrm_search_items import SearchUsers

from selenium.webdriver.common.by import By
import csv
import os
from random import randint


class CreateNewBudget(SuitecrmBasePage):

    BUDGETS = ''
    ACCESS_HOME = (By.LINK_TEXT, 'TODO')
    ACCESS_BUDGET = (By.LINK_TEXT, 'Presupuestos')
    CREATE_BUDGET = (By.LINK_TEXT, 'Crear Cotización')
    TITLE_BUDGET = (By.ID, 'name')
    OPPORTUNITY = (By.ID, 'btn_opportunity')
    NAME = (By.ID, 'name_advanced')
    VALID_UNTIL = (By.ID, 'expiration_trigger')
    WINDOW_VISIBLE = (By.ID, 'container_expiration_trigger_c')
    DATE = (By.XPATH, '//*[@id="expiration_trigger_div_t_cell30"]/a')
    STAGE = (By.ID, 'stage')
    VALUE_STAGE = 'On Hold'
    APPROVAL_ISSUE = (By.ID, 'approval_issue')
    NAME_ACCOUNT = (By.ID, 'btn_billing_account')
    SEARCH_ACCOUNT = (By.ID, 'name_advanced')
    SHIPPING_AMOUNT = (By.ID, 'shipping_amount')
    SHIPPING_TAX = (By.ID, 'shipping_tax')
    SAVE = (By.ID, 'SAVE')

    VIEW_CONTACT = (By.LINK_TEXT, 'Ver Cotizaciones')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[4]//a'

    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    SCREEN_VISIBLE = (By.ID, 'searchDialog')
    NAME_TITLE = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def __init__(self, driver):
        super().__init__(driver)

        file = open(os.getcwd() + "/data/Suitecrm_budgets.csv")
        content = csv.reader(file, delimiter=',')
        self.BUDGETS = list(content)
        file.close()

        self.TITLE = self.BUDGETS[1][0] + '-' + str(randint(100, 800))

    def create_new_budget(self):

        self.menu_select_option(self.ACCESS_HOME, self.ACCESS_BUDGET)

        self.wait_button_clickable(self.CREATE_BUDGET)

        self.click_button(self.CREATE_BUDGET)

        self.wait_selector_visible(self.TITLE_BUDGET)

        self.fill_text_field(self.TITLE_BUDGET, self.TITLE)

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.OPPORTUNITY
        find_data_page.selector_search_field = self.NAME
        find_data_page.search_query = self.BUDGETS[1][1]
        find_data_page.open_site_search()

        self.click_button(self.VALID_UNTIL)

        self.wait_button_clickable(self.WINDOW_VISIBLE)

        self.click_button(self.DATE)

        self.fill_select_field(self.STAGE, self.VALUE_STAGE)

        self.fill_text_field(self.APPROVAL_ISSUE, self.BUDGETS[1][3])

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.NAME_ACCOUNT
        find_data_page.selector_search_field = self.SEARCH_ACCOUNT
        #find_data_page.filled = True
        find_data_page.search_query = self.BUDGETS[1][2]
        find_data_page.open_site_search()

        self.fill_text_field(self.SHIPPING_AMOUNT, self.BUDGETS[1][10])

        self.fill_select_field(self.SHIPPING_TAX, self.BUDGETS[1][11])

        self.send_enter_key(self.SAVE)

    def get_title(self):

        return self.TITLE

    def search_budget(self, title):
        '''
        search_contact = SuitecrmSiteSearchElement(self.driver)
        search_contact.access_option = self.VIEW_CONTACT
        search_contact.press_filter = self.FILTER
        search_contact.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_contact.col_selector = self.COL_SELECTOR
        search_contact.name_selector = self.NAME_SELECTOR
        value = search_contact.search_element(title)

        return value
        '''
        search_contact = SearchUsers(self.driver)
        search_contact.access_option = self.VIEW_CONTACT
        search_contact.press_filter = self.FILTER
        search_contact.press_rapid_filter = self.RAPID_FILTER
        search_contact.visible_selector = self.SCREEN_VISIBLE
        search_contact.contact_name = self.NAME_TITLE

        value = search_contact.search_user(title)

        return value






