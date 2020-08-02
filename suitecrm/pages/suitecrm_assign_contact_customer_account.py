from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
import time


class AssignContactCustomerAccount(SuitecrmBasePage):

    BUTTON_CONTACT = (By.LINK_TEXT, 'CONTACTOS')
    CREATE_CONTACT = (By.LINK_TEXT, 'Seleccionar')
    ACCESS_SELECT = (By.XPATH, '//*[@id="list_subpanel_contacts"]/table//td/table/tbody//li/span')
    EMAIL = (By.ID, 'email_advanced')
    BUTTON_SEARCH = (By.XPATH, '//*[@id="search_form_submit"]')

    def assign_contact(self, contact_email, contact_name):

        self.window_scroll()

        self.menu_select_option(self.BUTTON_CONTACT, self.ACCESS_SELECT)

        select = self.driver.find_element(*self.CREATE_CONTACT)
        window_before = self.driver.window_handles[0]
        select.click()
        time.sleep(2)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        self.fill_text_field(self.EMAIL, contact_email)

        self.click_button(self.BUTTON_SEARCH)

        self.window_scroll()

        select_client = self.driver.find_element(By.PARTIAL_LINK_TEXT, contact_name)
        select_client.click()

        self.driver.switch_to.window(window_before)


