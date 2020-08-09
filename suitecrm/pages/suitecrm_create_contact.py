from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from pages.suitecrm_create_new_contact import CreateNewContact


class CreateContact(SuitecrmBasePage):

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

    VIEW_CONTACT = (By.LINK_TEXT, 'Ver Contactos')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[3]//a'

    def page_contact(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_CONTACT)

    def create_contact(self):

        contact = CreateNewContact(self.driver)
        contact.select_type = self.SELECT_TYPE
        contact.first_name = self.FIRST_NAME
        contact.surname = self.SURNAMES
        contact.telephone = self.TELEPHONE
        contact.mobile = self.MOBILE
        contact.work_station = self.WORKING_STATION
        contact.depart = self.DEPARTMENT
        contact.email = self.EMAIL
        contact.address = self.ADDRESS
        contact.city = self.CITY
        contact.cp = self.CP
        contact.country = self.COUNTRY
        contact.description = self.DESCRIPTION
        contact.copy = self.BUTTON_COPY
        contact.contact_point = self.CONTACT_POINT
        contact.save = self.SAVE
        contact.new_contact()
        email = contact.get_contact_email()
        complete_name = contact.get_contact_name()

        return email, complete_name

    def search_contact(self, contact_name):

        search_contact = SuitecrmSiteSearchElement(self.driver)
        search_contact.access_menu = self.VIEW_CONTACT
        search_contact.press_filter = self.FILTER
        search_contact.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_contact.col_selector = self.COL_SELECTOR
        search_contact.name_selector = self.NAME_SELECTOR
        value = search_contact.search_element(contact_name)

        return value










