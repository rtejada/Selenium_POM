from lib.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.by import By


class SearchUsers(SuitecrmBasePage):

    VIEW_USERS = (By.LINK_TEXT, 'Ver Usuarios')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'search_name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def search_user(self, user):
        pass
        '''

        self.click_button(self.VIEW_USERS)

        self.wait_selector_visible(self.FILTER)

        self.click_button(self.FILTER)

        self.wait_selector_visible(self.WINDOW_VISIBLE)

        self.click_button(self.RAPID_FILTER)

        self.wait_selector_visible(self.BUTTON_NAME)

        self.fill_text_field(self.BUTTON_NAME, user)

        self.send_enter_key(self.SEARCH)

        self.click_button((By.LINK_TEXT, user))

        user = self.driver.find_element_by_xpath('//a[@title = "Filtro"]//*[@id="full_name"]')

        return user.text
'''