from pages.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.by import By


class SearchContact(SuitecrmBasePage):

    MENU_SALES = (By.LINK_TEXT, 'VENTAS')
    ACCESS_CONTACT = (By.LINK_TEXT, 'Contactos')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    WAIT_LOCATOR = (By. XPATH, "//ul[@class='nav nav-tabs']/li/a[@aria-expanded='true']")
    RAPID_FILTER = (By. XPATH, "//ul[@class='nav nav-tabs']/li/a[@aria-expanded='true']")
    BUTTON_NAME = (By.ID, 'search_name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def search_contact(self, contact_email, contact_name):
        self.menu_select_option(self.MENU_SALES, self.ACCESS_CONTACT)

        self.click_button(self.FILTER)

        #ventana javscript

        self.click_button(self.RAPID_FILTER)

        self.fill_text_field(self.BUTTON_NAME, contact_name)

        self.button_save(self.SEARCH)





