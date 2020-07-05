from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
from random import randint


class CreateNewContact(SuitecrmBasePage):

    CONTACTS = {'gender_type': 'Mrs.', 'type_contact': 'Other', 'name': 'Maria', 'surnames': 'Molinero Molinero', 'tel': '730-8298', 'mobile': '689457896', 'workingStation': 'Comercial',
                'departament': 'Pruebas', 'email': '@hotmail.com', 'address': '321 University Ave-', 'city': 'Alcorcon', 'CP': '28925',
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
    EMAIL = (By.ID, 'Contacts0emailAddress0')
    ADDRESS = (By.ID, 'primary_address_street')
    CITY = (By.ID, 'primary_address_city')
    CP = (By.ID, 'primary_address_postalcode')
    COUNTRY = (By.ID, 'primary_address_country')
    DESCRIPTION = (By.ID, 'description')
    BUTTON_COPY = (By.ID, 'alt_checkbox')
    CONTACT_POINT = (By.ID, 'lead_source')
    SAVE = (By.ID, 'SAVE')

    def __init__(self, driver):
        super().__init__(driver)
        self.CONTACTS['surnames'] = self.CONTACTS['surnames'] + str(randint(1, 90000000))
        self.CONTACTS['email'] = str(randint(1, 90000000)) + (self.CONTACTS['email'])

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

        self.fill_select_field(self.SELECT_TYPE, self.CONTACTS['gender_type'])

        self.fill_text_field(self.FIRST_NAME, self.CONTACTS['name'])

        self.fill_text_field(self.SURNAMES, self.CONTACTS['surnames'])

        self.fill_text_field(self.TELEPHONE, self.CONTACTS['tel'])

        self.fill_text_field(self.MOBILE, self.CONTACTS['mobile'])

        self.fill_text_field(self.WORKING_STATION, self.CONTACTS['workingStation'])

        self.fill_text_field(self.DEPARTMENT, self.CONTACTS['departament'])

        self.fill_text_field(self.EMAIL, self.CONTACTS['email'])

        self.fill_text_field(self.ADDRESS, self.CONTACTS['address'])

        self.fill_text_field(self.CITY, self.CONTACTS['city'])

        self.fill_text_field(self.CP, self.CONTACTS['CP'])

        self.fill_text_field(self.COUNTRY, self.CONTACTS['country'])

        self.fill_text_field(self.DESCRIPTION, self.CONTACTS['description'])

        self.click_button_copy(self.BUTTON_COPY)

        self.fill_select_field(self.CONTACT_POINT, self.CONTACTS['type_contact'])

        self.button_save(self.SAVE)


    def get_search_string(self):

        return self.CONTACTS['name'] + self.CONTACTS['surnames']





        '''
        ACCOUNT_BUTTON = (By.ID, 'btn_account_name')
        select_account_button = self.driver.find_element(*self.ACCOUNT_BUTTON)
        select_account_button.click()
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        '''







