from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By
import csv


class CreateNewBudget(SuitecrmBasePage):

    BUDGETS = ''
    ACCESS_HOME = (By.LINK_TEXT, 'TODO')
    ACCESS_BUDGET = (By.LINK_TEXT, 'Presupuestos')
    CREATE_BUDGET = (By.LINK_TEXT, 'Crear Cotización')
    TITLE_BUDGET = (By.ID, 'name')
    OPPORTUNITY = (By.ID, 'btn_opportunity')
    NAME = (By.ID, 'name_advanced')
    VALID_UNTIL = (By.ID, 'expiration_trigger')
    DATE = (By.ID, 'expiration_trigger_div_t_cell36')
    STAGE = (By.ID, 'stage')
    VALUE_STAGE = 'On Hold'
    APPROVAL_ISSUE = (By.ID, 'approval_issue')
    NAME_ACCOUNT = (By.ID, 'btn_billing_account')

    TOTAl = (By.ID, 'total_amt')
    DISCOUNT = (By.ID, 'discount_amount')
    SUBTOTAL = (By.ID, 'subtotal_amount')
    SHIPPING_AMOUNT = (By.ID, 'shipping_amount')
    SHIPPING_TAX = (By.ID, 'shipping_tax_amt')
    TAX_AMOUNT = (By.ID, 'tax_amount')
    TOTAL_AMOUNT = (By.ID, 'total_amount')

    SAVE = (By.ID, 'SAVE')

    def __init__(self, driver):
        super().__init__(driver)

        file = open('../data/Suitecrm_budgets.csv')
        content = csv.reader(file, delimiter=',')
        self.BUDGETS = list(content)
        file.close()

    def create(self):

        self.menu_select_option(self.ACCESS_HOME, self.ACCESS_BUDGET)

        self.wait_button_clickable(self.CREATE_BUDGET)

        self.click_button(self.CREATE_BUDGET)

        self.wait_selector_visible(self.TITLE_BUDGET)

        self.fill_text_field(self.TITLE_BUDGET, self.BUDGETS[1][0])

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.OPPORTUNITY
        find_data_page.selector_search_field = self.NAME
        find_data_page.search_query = self.BUDGETS[1][1]
        find_data_page.open_site_search()

        self.click_button(self.VALID_UNTIL)

        self.wait_button_clickable(self.DATE)

        self.click_button(self.DATE)

        self.fill_select_field(self.STAGE, self.VALUE_STAGE)

        self.fill_text_field(self.APPROVAL_ISSUE, self.BUDGETS[1][3])

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.NAME_ACCOUNT
        find_data_page.filled = True
        find_data_page.search_query = self.BUDGETS[1][2]
        find_data_page.open_site_search()

        self.fill_text_field(self.TOTAl, self.BUDGETS[1][8])

        self.fill_text_field(self.DISCOUNT, self.BUDGETS[1][9])

        self.fill_text_field(self.SUBTOTAL, self.BUDGETS[1][10])

        self.fill_text_field(self.SHIPPING_AMOUNT, self.BUDGETS[1][11])

        self.fill_text_field(self.SHIPPING_TAX, self.BUDGETS[1][12])

        self.fill_text_field(self.TAX_AMOUNT, self.BUDGETS[1][13])

        self.fill_text_field(self.TOTAL_AMOUNT, self.BUDGETS[1][14])

        self.send_enter_key(self.SAVE)







