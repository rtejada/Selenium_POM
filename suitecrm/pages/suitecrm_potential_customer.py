from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_items import SearchUsers
from pages.suitecrm_create_new_potent_custom import CreateNew


class PotentialCustomer(SuitecrmBasePage):

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_POTENTIAL_CUSTOMER = (By.LINK_TEXT, 'Crear Clientes Potenciales')

    POTENTIAL_CLIENTS = (By.LINK_TEXT, 'Ver Clientes Potenciales')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'search_name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def page_account(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_POTENTIAL_CUSTOMER)

    def create(self):

        potential_customer = CreateNew(self.driver)
        name = potential_customer.customer()
        return name

    def search(self, potential_customer):

        self.wait_selector_visible(self.POTENTIAL_CLIENTS)

        search_opportunity = SearchUsers(self.driver)
        search_opportunity.access_option = self.POTENTIAL_CLIENTS
        search_opportunity.press_filter = self.FILTER
        search_opportunity.press_rapid_filter = self.RAPID_FILTER
        search_opportunity.visible_selector = self.WINDOW_VISIBLE
        search_opportunity.contact_name = self.BUTTON_NAME
        value = search_opportunity.search_user(potential_customer)
        return value
