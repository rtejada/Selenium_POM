from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from pages.suitecrm_create_new_account_customer import CreateNewCustomerAccount


class CustomerAccount(SuitecrmBasePage):

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_CONTACT = (By.LINK_TEXT, 'Crear Cuentas')

    ACCOUNTS = (By.LINK_TEXT, 'Ver Cuentas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[3]//a'

    def page_account(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_CONTACT)

    def create_customer_account(self):

        customer = CreateNewCustomerAccount(self.driver)
        customer.create_customer_account()
        email = customer.get_customer_email()
        name = customer.get_customer_name()

        return email, name

    def search_customer(self, account):

        customer = SuitecrmSiteSearchElement(self.driver)
        customer.access_option = self.ACCOUNTS
        customer.press_filter = self.FILTER
        customer.table_rows_selector = self.TABLE_ROWS_SELECTOR
        customer.name_selector = self.NAME_SELECTOR
        customer.col_selector = self.COL_SELECTOR
        value = customer.search_element(account)

        return value

