from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
from random import randint


class CreateNewContact(SuitecrmBasePage):

    CONTACTS = {'gender_type': 'Mrs.', 'type_contact': 'Other', 'name': 'Toulouse', 'surnames': 'Tournefeuille', 'tel': '034-829875', 'mobile': '689457815', 'workingStation': 'Administrativo',
                'departament': 'Toulose_Depart', 'email': '@toulouse.fr', 'address': '138 Saint-Geniès-Bellevue', 'city': 'Saint-Bellevue', 'CP': '31200',
                'country': 'Francia', 'description': 'Esperas explícitas disponibles para clientes de Selenium'}

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
        self.CONTACTS['surnames'] = self.CONTACTS['surnames'] + ' ' + str(randint(1, 90000000))
        self.CONTACTS['email'] = str(randint(1, 90000000)) + (self.CONTACTS['email'])

    def page_contact(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_CONTACT)

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

        self.click_button(self.BUTTON_COPY)

        self.fill_select_field(self.CONTACT_POINT, self.CONTACTS['type_contact'])

        self.send_enter_key(self.SAVE)

    def get_contact_email(self):

        return self.CONTACTS['email']

    def get_contact_name(self):

        return self.CONTACTS['name'] + ' ' + self.CONTACTS['surnames']









