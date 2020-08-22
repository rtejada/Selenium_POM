from lib.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.by import By

class SearchCustomer(SuitecrmBasePage):

    MENU_SALES = (By.LINK_TEXT, 'VENTAS')
    ACCESS_ACCOUNT = (By.LINK_TEXT, 'Cuentas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def search_customer(self, customer):

        self.menu_select_option(self.MENU_SALES, self.ACCESS_ACCOUNT)

        self.wait_selector_visible(self.FILTER)

        self.click_button(self.FILTER)

        self.wait_selector_visible(self.WINDOW_VISIBLE)

        self.click_button(self.RAPID_FILTER)

        self.wait_selector_visible(self.BUTTON_NAME)

        self.fill_text_field(self.BUTTON_NAME, customer)

        self.send_enter_key(self.SEARCH)

        self.click_button((By.LINK_TEXT, customer))

        return customer


