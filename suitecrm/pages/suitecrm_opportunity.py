from lib.suitecrm_base_page import SuitecrmBasePage
from pages.suitecrm_create_new_opportunity import CreateNewOpportunity
from lib.suitecrm_search_items import SearchUsers
from selenium.webdriver.common.by import By


class CreateOpportunity(SuitecrmBasePage):

    OPPORTUNITY = ''
    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_OPPORTUNITY = (By.LINK_TEXT, 'Crear Oportunidades')

    VIEW_OPPORTUNITY = (By.LINK_TEXT, 'Ver Oportunidades')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def access(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_OPPORTUNITY)

    def create(self):

        opportunity = CreateNewOpportunity(self.driver)
        opportunity.create()
        name = opportunity.get_name()

        return name

    def search(self, name_opportunity):

        search_opportunity = SearchUsers(self.driver)
        search_opportunity.access_option = self.VIEW_OPPORTUNITY
        search_opportunity.press_filter = self.FILTER
        search_opportunity.press_rapid_filter = self.RAPID_FILTER
        search_opportunity.visible_selector = self.WINDOW_VISIBLE
        search_opportunity.contact_name = self.BUTTON_NAME
        value = search_opportunity.search_user(name_opportunity)
        return value











