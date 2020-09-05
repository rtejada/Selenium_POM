from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_items import SearchUsers
from pages.suitecrm_create_new_potent_custom import CreateNew


class PotentialCustomer(SuitecrmBasePage):

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_POTENTIAL_CUSTOMER = (By.LINK_TEXT, 'Crear Clientes Potenciales')

    ACCOUNTS = (By.LINK_TEXT, 'Ver Cuentas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def page_account(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_POTENTIAL_CUSTOMER)

    def create_potential_customer(self):

        potential_customer = CreateNew(self.driver)
        potential_customer.create()
