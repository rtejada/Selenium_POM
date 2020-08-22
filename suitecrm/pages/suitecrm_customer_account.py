from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_items import SearchUsers
from pages.suitecrm_create_new_account_customer import CreateNewCustomerAccount


class CustomerAccount(SuitecrmBasePage):

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_CONTACT = (By.LINK_TEXT, 'Crear Cuentas')

    ACCOUNTS = (By.LINK_TEXT, 'Ver Cuentas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def page_account(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_CONTACT)

    def create_customer_account(self):

        customer = CreateNewCustomerAccount(self.driver)
        customer.create_customer_account()
        email = customer.get_customer_email()
        name = customer.get_customer_name()

        return email, name

    def search_account(self, account):

        search_opportunity = SearchUsers(self.driver)
        search_opportunity.access_option = self.ACCOUNTS
        search_opportunity.press_filter = self.FILTER
        search_opportunity.press_rapid_filter = self.RAPID_FILTER
        search_opportunity.visible_selector = self.WINDOW_VISIBLE
        search_opportunity.contact_name = self.BUTTON_NAME
        value = search_opportunity.search_user(account)
        return value

