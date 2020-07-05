from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
from random import randint

class CreateCustomerAccount(SuitecrmBasePage):

    CUSTOMER_ACCOUNTS = {'type': 'Customer', 'type_industry': 'Communications', 'name': 'Industrias PRUEBAS', 'tel': '730-8298', 'web': 'www.prueba.com', 'email': '@pruebas.com',
                'address': '321 University Ave-', 'city': 'Alcorcon', 'CP': '28925', 'country': 'España',
                'description': 'Ninguna', 'annual_revenue': '1000000', 'employees': '40'}

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_CONTACT = (By.LINK_TEXT, 'Crear Cuentas')
    FIRST_NAME = (By.ID, 'name')
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
        self.CUSTOMER_ACCOUNTS['name'] = self.CUSTOMER_ACCOUNTS['name'] + ' ' + str(randint(1, 90000000))
        self.CUSTOMER_ACCOUNTS['email'] = str(randint(1, 90000000)) + (self.CUSTOMER_ACCOUNTS['email'])

    def page_account(self):

        select_button_create = self.driver.find_element(*self.BUTTON_CREATE)
        select_button_create.click()

        action = ActionChains(self.driver)
        action.move_to_element(select_button_create).perform()

        access_create_contact = self.driver.find_element(*self.CREATE_CONTACT)
        action.move_to_element(access_create_contact)
        action.click()
        action.perform()

    def create_customer_account(self):

        self.fill_text_field(self.FIRST_NAME, self.CUSTOMER_ACCOUNTS['name'])

        self.fill_text_field(self.TELEPHONE, self.CUSTOMER_ACCOUNTS['tel'])

        self.fill_text_field(self.WEB, self.CUSTOMER_ACCOUNTS['web'])

        self.fill_text_field(self.EMAIL, self.CUSTOMER_ACCOUNTS['email'])

        self.fill_text_field(self.ADDRESS, self.CUSTOMER_ACCOUNTS['address'])

        self.fill_text_field(self.CITY, self.CUSTOMER_ACCOUNTS['city'])

        self.fill_text_field(self.CP, self.CUSTOMER_ACCOUNTS['CP'])

        self.fill_text_field(self.COUNTRY, self.CUSTOMER_ACCOUNTS['country'])

        self.fill_text_field(self.DESCRIPTION, self.CUSTOMER_ACCOUNTS['description'])

        self.click_button(self.BUTTON_COPY)

        self.fill_select_field(self.TYPE_ACCOUNT, self.CUSTOMER_ACCOUNTS['type'])

        self.fill_select_field(self.INDUSTRY, self.CUSTOMER_ACCOUNTS['type_industry'])

        self.fill_text_field(self.ANNUAL_REVENUE, self.CUSTOMER_ACCOUNTS['annual_revenue'])

        self.fill_text_field(self.EMPLOYEES, self.CUSTOMER_ACCOUNTS['employees'])

        self.button_save(self.SAVE)

    def get_customer_email(self):

        return self.CUSTOMER_ACCOUNTS['email']

    def get_customer_name(self):

        return self.CUSTOMER_ACCOUNTS['name']
