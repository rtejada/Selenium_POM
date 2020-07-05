from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pages.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.keys import Keys


class AssignContactCustomerAccount(SuitecrmBasePage):
    CONTACTS = {'name': 'Maria Molinero', 'tel': '730-8298', 'mobile': '689457896', 'workingStation': 'Comercial',
                'departament': 'Pruebas', 'email': 'prueba@hotmail.com', 'address': '321 University Ave-',
                'city': 'Alcorcon', 'CP': '28925', 'country': 'España', 'description': 'Ninguna'}

    BUTTON_ACTIONS = (By.LINK_TEXT, 'Acciones')
    EDIT = (By.ID, 'edit_button')
    NEW_SCREEN = (By.XPATH, '//*[@id="btn_parent_name"]/span')
    NAME = (By.ID, 'name_advanced')
    BUTTON_SEARCH = (By.XPATH, '//*[@id="search_form_submit"]')

    def assign_contact(self, contact_search_string):
        select_button_actions = self.driver.find_element(*self.BUTTON_ACTIONS)
        select_button_actions.click()

        action = ActionChains(self.driver)
        action.move_to_element(select_button_actions).perform()

        access_edit = self.driver.find_element(*self.EDIT)
        action.move_to_element(access_edit)
        action.click()
        action.perform()

        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        search_contact = self.driver.find_element(*self.NEW_SCREEN)
        window_before = self.driver.window_handles[0]
        search_contact.click()
        window_after = self.driver.window_handles[1]

        self.driver.switch_to.window(window_after)
        search_name = self.driver.find_element(*self.NAME)
        search_name.click()
        search_name.send_keys(contact_search_string)

        search = self.driver.find_element(*self.BUTTON_SEARCH)
        search.click()

        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        select_client = self.driver.find_element((By.LINK_TEXT, contact_search_string))
        select_client.click()

        self.driver.switch_to.window(window_before)



