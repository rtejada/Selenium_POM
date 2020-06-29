from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.suitecrm_base_page import SuitecrmBasePage


class CreateNewContact(SuitecrmBasePage):

    CONTACTS = {'name': 'Maria', 'surnames': 'Molinero Molinero', 'tel': '730-8298', 'mobile': '689457896', 'workingStation': 'Comercial',
                'departament': 'Pruebas', 'email': 'prueba@hotmail.com', 'address': '321 University Ave-', 'city': 'Alcorcon', 'CP': '28925',
                'country': 'España', 'description': 'Ninguna'}

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_CONTACT = (By.LINK_TEXT, 'Crear Contactos')

    SELECT_TYPE = (By.ID, 'salutation')
    FIRST_NAME = (By.NAME, 'first_name')
    SURNAMES = (By.NAME, 'last_name')
    TELEPHONE = (By.ID, 'phone_work')
    MOBILE = (By.ID, 'phone_mobile')
    WORKING_STATION = (By.ID, 'title')
    DEPARTMENT = (By.ID, 'department')
    EMAIL = (By.ID, 'Contacts0emailAddress0' )
    ADDRESS = (By.ID, 'primary_address_street')
    CITY = (By.ID, 'primary_address_city')
    CP = (By.ID, 'primary_address_postalcode')
    COUNTRY = (By.ID, 'primary_address_country')
    DESCRIPTION = (By.ID, 'description')
    BUTTON_COPY = (By.ID, 'alt_checkbox')

    def page_contact(self):
        select_button_create = self.driver.find_element(*self.BUTTON_CREATE)
        select_button_create.click()
        action = ActionChains(self.driver)
        action.move_to_element(select_button_create).perform()
        access_create_contact = self.driver.find_element(*self.CREATE_CONTACT)
        action.move_to_element(access_create_contact)
        action.click()
        action.perform()

    def create_new_contact(self):
        type_new_contact = self.driver.find_element(*self.SELECT_TYPE)
        type_select = Select(type_new_contact)
        type_select.select_by_value('Mrs.')

        name = self.driver.find_element(*self.FIRST_NAME)
        name.click()
        name.send_keys(self.CONTACTS['name'])

        surname = self.driver.find_element(*self.SURNAMES)
        surname.click()
        surname.send_keys(self.CONTACTS['surnames'])

        telephone = self.driver.find_element(*self.TELEPHONE)
        telephone.click()
        telephone.send_keys(self.CONTACTS['tel'])

        mobile = self.driver.find_element(*self.MOBILE)
        mobile.click()
        mobile.send_keys(self.CONTACTS['mobile'])

        work_station = self.driver.find_element(*self.WORKING_STATION)
        work_station.click()
        work_station.send_keys(self.CONTACTS['workingStation'])

        department = self.driver.find_element(*self.DEPARTMENT)
        department.click()
        department.send_keys(self.CONTACTS['departament'])

        email = self.driver.find_element(*self.EMAIL)
        email.click()
        email.send_keys(self.CONTACTS['email'])

        address = self.driver.find_element(*self.ADDRESS)
        address.click()
        address.send_keys(self.CONTACTS['address'])

        city = self.driver.find_element(*self.CITY)
        city.click()
        city.send_keys(self.CONTACTS['city'])

        cp = self.driver.find_element(*self.CP)
        cp.click()
        cp.send_keys(self.CONTACTS['CP'])

        country = self.driver.find_element(*self.COUNTRY)
        country.click()
        country.send_keys(self.CONTACTS['country'])

        description = self.driver.find_element(*self.DESCRIPTION)
        description.click()
        description.send_keys(self.CONTACTS['description'])

        button_copy = self.driver.find_element(*self.BUTTON_COPY)
        button_copy.click()





        '''
        ACCOUNT_BUTTON = (By.ID, 'btn_account_name')
        select_account_button = self.driver.find_element(*self.ACCOUNT_BUTTON)
        select_account_button.click()
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        '''







