from pages.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.by import By


class SearchContact(SuitecrmBasePage):

    MENU_SALES = (By.LINK_TEXT, 'VENTAS')
    ACCESS_CONTACT = (By.LINK_TEXT, 'Contactos')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By. LINK_TEXT, 'Filtro rápido')
    BUTTON_NAME = (By.ID, 'search_name_basic')
    SEARCH = (By.ID, 'search_form_submit')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_ACTIONS = (By.XPATH, '//*[@id="tab-actions"]/a')

    def search_contact(self, contact_email, contact_name):
        self.wait_selector_visible(self.MENU_SALES)

        self.menu_select_option(self.MENU_SALES, self.ACCESS_CONTACT)

        self.wait_button_clickable(self.FILTER)

        self.click_button(self.FILTER)

        self.wait_selector_visible(self.WINDOW_VISIBLE)

        self.click_button(self.RAPID_FILTER)

        self.wait_selector_visible(self.BUTTON_NAME)

        self.fill_text_field(self.BUTTON_NAME, contact_name)

        self.button_save(self.SEARCH)

        self.click_button((By.PARTIAL_LINK_TEXT, contact_name))

        self.wait_button_clickable(self.BUTTON_ACTIONS)







