from lib.suitecrm_base_page import SuitecrmBasePage
from random import randint


class CreateNewContact(SuitecrmBasePage):
    CONTACTS = {'gender_type': 'Mrs.', 'type_contact': 'Other', 'name': 'Toulouse', 'surnames': 'Feuille',
                'tel': '034-829875', 'mobile': '689457815', 'workingStation': 'Administrativo',
                'departament': 'Toulose_Depart', 'email': '@toulouse.fr', 'address': '138 Saint-Geniès-Bellevue',
                'city': 'Saint-Bellevue', 'CP': '31200',
                'country': 'Francia', 'description': 'Esperas explícitas disponibles para clientes de Selenium'}

    select_type = ''
    first_name = ''
    surname = ''
    telephone = ''
    mobile = ''
    work_station = ''
    depart = ''
    email = ''
    address = ''
    city = ''
    cp = ''
    country = ''
    description = ''
    copy = ''
    contact_point = ''
    save = ''

    def __init__(self, driver):
        super().__init__(driver)
        self.CONTACTS['surnames'] = self.CONTACTS['surnames'] + ' ' + str(randint(1, 90000000))
        self.CONTACTS['email'] = str(randint(1, 90000000)) + (self.CONTACTS['email'])

    def new_contact(self):

        self.fill_select_field(self.select_type, self.CONTACTS['gender_type'])

        self.fill_text_field(self.first_name, self.CONTACTS['name'])

        self.fill_text_field(self.surname, self.CONTACTS['surnames'])

        self.fill_text_field(self.telephone, self.CONTACTS['tel'])

        self.fill_text_field(self.mobile, self.CONTACTS['mobile'])

        self.fill_text_field(self.work_station, self.CONTACTS['workingStation'])

        self.fill_text_field(self.depart, self.CONTACTS['departament'])

        self.fill_text_field(self.email, self.CONTACTS['email'])

        self.fill_text_field(self.address, self.CONTACTS['address'])

        self.fill_text_field(self.city, self.CONTACTS['city'])

        self.fill_text_field(self.cp, self.CONTACTS['CP'])

        self.fill_text_field(self.country, self.CONTACTS['country'])

        self.fill_text_field(self.description, self.CONTACTS['description'])

        self.click_button(self.copy)

        self.fill_select_field(self.contact_point, self.CONTACTS['type_contact'])

        self.send_enter_key(self.save)

    def get_contact_email(self):

        return self.CONTACTS['email']

    def get_contact_name(self):

        return self.CONTACTS['name'] + ' ' + self.CONTACTS['surnames']