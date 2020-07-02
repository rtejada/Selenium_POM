from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.keys import Keys


class CreateCustomerAccount(SuitecrmBasePage):

    CUSTOMER_ACCOUNTS = {'name': 'Maria Molinero', 'tel': '730-8298', 'web': 'www.prueba.com', 'email': 'prueba@hotmail.com',
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

        name = self.driver.find_element(*self.FIRST_NAME)
        name.click()
        name.send_keys(self.CUSTOMER_ACCOUNTS['name'])

        telephone = self.driver.find_element(*self.TELEPHONE)
        telephone.click()
        telephone.send_keys(self.CUSTOMER_ACCOUNTS['tel'])

        page_web = self.driver.find_element(*self.WEB)
        page_web.click()
        page_web.send_keys(self.CUSTOMER_ACCOUNTS['web'])

        email = self.driver.find_element(*self.EMAIL)
        email.click()
        email.send_keys(self.CUSTOMER_ACCOUNTS['email'])

        address = self.driver.find_element(*self.ADDRESS)
        address.click()
        address.send_keys(self.CUSTOMER_ACCOUNTS['address'])

        city = self.driver.find_element(*self.CITY)
        city.click()
        city.send_keys(self.CUSTOMER_ACCOUNTS['city'])

        cp = self.driver.find_element(*self.CP)
        cp.click()
        cp.send_keys(self.CUSTOMER_ACCOUNTS['CP'])

        country = self.driver.find_element(*self.COUNTRY)
        country.click()
        country.send_keys(self.CUSTOMER_ACCOUNTS['country'])

        description = self.driver.find_element(*self.DESCRIPTION)
        description.click()
        description.send_keys(self.CUSTOMER_ACCOUNTS['description'])

        button_copy = self.driver.find_element(*self.BUTTON_COPY)
        button_copy.click()

        type_account = self.driver.find_element(*self.TYPE_ACCOUNT)
        select_type = Select(type_account)
        select_type.select_by_value('Customer')

        type_industry = self.driver.find_element(*self.INDUSTRY)
        select_type_industry = Select(type_industry)
        select_type_industry.select_by_value('Communications')

        annual_revenue = self.driver.find_element(*self.ANNUAL_REVENUE)
        annual_revenue.click()
        annual_revenue.send_keys(self.CUSTOMER_ACCOUNTS['annual_revenue'])

        employees = self.driver.find_element(*self.EMPLOYEES)
        employees.click()
        employees.send_keys(self.CUSTOMER_ACCOUNTS['employees'])

        save = self.driver.find_element(*self.SAVE)
        save.send_keys(Keys.ENTER)

