from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from pages.suitecrm_create_new_opportunity import CreateNewOpportunity
from selenium.webdriver.common.by import By


class CreateOpportunity(SuitecrmBasePage):

    OPPORTUNITY = ''
    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_OPPORTUNITY = (By.LINK_TEXT, 'Crear Oportunidades')

    VIEW_OPPORTUNITY = (By.LINK_TEXT, 'Ver Oportunidades')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[3]//a'

    def access(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_OPPORTUNITY)

    def create(self):

        opportunity = CreateNewOpportunity(self.driver)
        opportunity.create()
        name = opportunity.get_name()

        return name

    def search(self, name_opportunity):
        search_contact = SuitecrmSiteSearchElement(self.driver)
        search_contact.access_option = self.VIEW_OPPORTUNITY
        search_contact.press_filter = self.FILTER
        search_contact.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_contact.col_selector = self.COL_SELECTOR
        search_contact.name_selector = self.NAME_SELECTOR
        value = search_contact.search_element(name_opportunity)

        return value









