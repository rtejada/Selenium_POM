from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage


class AssignContactCustomerAccount(SuitecrmBasePage):

    BUTTON_CONTACT = (By.LINK_TEXT, 'CONTACTOS')
    CREATE_CONTACT = (By.LINK_TEXT, 'Seleccionar')
    ACCESS_SELECT = (By.XPATH, "//li/span[@class ='suitepicon suitepicon-action-caret']")
    EMAIL = (By.ID, 'email_advanced')
    BUTTON_SEARCH = (By.XPATH, '//*[@id="search_form_submit"]')

    def assign_contact(self, client_email, data_client):

        self.window_scroll()

        select_button_actions = self.driver.find_element(*self.BUTTON_CONTACT)
        select_button_actions.click()

        action = ActionChains(self.driver)
        action.move_to_element(select_button_actions).perform()

        access_to_select = self.driver.find_element(*self.ACCESS_SELECT)
        action.move_to_element(access_to_select)
        action.click()
        action.perform()

        select = self.driver.find_element(*self.CREATE_CONTACT)
        window_before = self.driver.window_handles[0]
        select.click()

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        self.fill_text_field(self.EMAIL, client_email)

        self.click_button(self.BUTTON_SEARCH)

        self.window_scroll()

        select_client = self.driver.find_element(By.PARTIAL_LINK_TEXT, data_client)
        select_client.click()

        self.driver.switch_to.window(window_before)


