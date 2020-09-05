from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
import json
import os
from random import randint


class CreateNew(SuitecrmBasePage):

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_CONTACT = (By.LINK_TEXT, 'Crear Cuentas')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    TELEPHONE = (By.ID, 'phone_office')
    WEB = (By.ID, 'website')
    EMAIL = (By.ID, 'Accounts0emailAddress0')
    ADDRESS = (By.ID, 'billing_address_street')
    CITY = (By.ID, 'billing_address_city')
    CP = (By.ID, 'billing_address_postalcode')
    COUNTRY = (By.ID, 'billing_address_country')
    DESCRIPTION = (By.ID, 'description')
    BUTTON_COPY = (By.ID, 'shipping_checkbox')
    TYPE_ACCOUNT = (By.ID, 'account_type')
    INDUSTRY = (By.ID, 'industry')

    ANNUAL_REVENUE = (By.ID, 'annual_revenue')
    EMPLOYEES = (By.ID, 'employees')
    SAVE = (By.ID, 'SAVE')

    def __init__(self, driver):
        super().__init__(driver)
        
        with open(os.getcwd() + "/data/data_potential_customer.json") as file:
            self.LIST_POT_CUSTOM = json.load(file)

        self.FULL_NAME = self.LIST_POT_CUSTOM['full_name']
        self.first_name = self.FULL_NAME[0] + self.random_letter(5)
        self.last_name = self.FULL_NAME[1] + self.random_letter(5)

    def create(self):

        self.fill_text_field(self.FIRST_NAME, self.first_name)

        self.fill_text_field(self.LAST_NAME, self.last_name)



