from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage


class SearchCustomer(SuitecrmBasePage):

    MENU_SALES = (By.LINK_TEXT, 'VENTAS')
    ACCESS_ACCOUNT = (By.LINK_TEXT, 'Cuentas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    WAIT_LOCATOR = (By.XPATH, "//ul[@class='nav nav-tabs']/li/a[@aria-expanded='true']")
    RAPID_FILTER = (By.XPATH, "//ul[@class='nav nav-tabs']/li/a[@aria-expanded='true']")
    BUTTON_NAME = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def search_customer(self, customer_email, customer_name):

        self.menu_select_option(self.MENU_SALES, self.ACCESS_ACCOUNT)

        self.wait_selector_visible(self.FILTER)

        self.click_button(self.FILTER)

        self.click_button(self.RAPID_FILTER)

        self.fill_text_field(self.BUTTON_NAME, customer_name)

        self.button_save(self.SEARCH)
