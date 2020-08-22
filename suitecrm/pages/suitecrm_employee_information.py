from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By
import json
import os
from random import randint


class FillEmployeeInfo(SuitecrmBasePage):

    DATA_USERS = ''

    EMPLOYEE_INFO = {"TITLE_EMPLOYEE": (By.ID, 'title'), "PHONE_WORK": (By.ID, 'phone_work'), "PHONE_MOBILE": (By.ID, 'phone_mobile'),
                     "DEPARTMENT": (By.ID, 'department'), "INFO": (By.ID, 'btn_reports_to_name'), "NAME": (By.ID, 'first_name_advanced'),
                     "PHONE_OTHER": (By.ID, 'phone_other'), "FAX": (By.ID, 'phone_fax'), "HOME_PHONE": (By.ID, 'phone_home'),
                     "MESSENGER_TYPE": (By.ID, 'messenger_type'), "MESSENGER_ACCOUNT": (By.ID, 'messenger_id'),
                     "ADDRESS_STREET": (By.ID, 'address_street'), "ADDRESS_CITY": (By.ID, 'address_city'),
                     "ADDRESS_STATE": (By.ID, 'address_state'), "CP": (By.ID, 'address_postalcode'),
                     "ADDRESS_COUNTRY": (By.ID, 'address_country'), "DESCRIPTION": (By.ID, 'description'),
                     "EMAIL": (By.ID, 'Users0emailAddress0')
                     }

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/data/data_users.json") as data:
            self.DATA_USERS = json.load(data)

        self.EMAIL = str(randint(10000, 20000)) + self.DATA_USERS['email']

    def fill(self):

        self.fill_text_field(self.EMPLOYEE_INFO['TITLE_EMPLOYEE'], self.DATA_USERS['Job_title'])

        self.fill_text_field(self.EMPLOYEE_INFO['PHONE_WORK'], self.DATA_USERS['phone_work'])

        self.fill_text_field(self.EMPLOYEE_INFO['PHONE_MOBILE'], self.DATA_USERS['cell_phone'])

        self.fill_text_field(self.EMPLOYEE_INFO['DEPARTMENT'], self.DATA_USERS['department'])

        find_data_page = SuitecrmSiteSearch(self.driver)
        find_data_page.selector_open_window = self.EMPLOYEE_INFO['INFO']
        find_data_page.selector_search_field = self.EMPLOYEE_INFO['NAME']
        find_data_page.search_query = self.DATA_USERS['inform_a']
        find_data_page.open_site_search()

        self.fill_text_field(self.EMPLOYEE_INFO['PHONE_OTHER'], self.DATA_USERS['another_phone'])

        self.fill_text_field(self.EMPLOYEE_INFO['FAX'], self.DATA_USERS['fax'])

        self.fill_text_field(self.EMPLOYEE_INFO['HOME_PHONE'], self.DATA_USERS['home_phone'])

        self.fill_select_by_text(self.EMPLOYEE_INFO['MESSENGER_TYPE'], self.DATA_USERS['type_of_instant_msn'])

        self.fill_text_field(self.EMPLOYEE_INFO['MESSENGER_ACCOUNT'], self.DATA_USERS['instant_msn_account'])

        self.window_scroll_half()

        self.fill_text_field(self.EMPLOYEE_INFO['ADDRESS_CITY'], self.DATA_USERS['address_city'])

        self.fill_text_field(self.EMPLOYEE_INFO['CP'], self.DATA_USERS['cp'])

        self.fill_text_field(self.EMPLOYEE_INFO['ADDRESS_STREET'], self.DATA_USERS['street_address'])

        self.fill_text_field(self.EMPLOYEE_INFO['ADDRESS_STATE'], self.DATA_USERS['state_prov_address'])

        self.fill_text_field(self.EMPLOYEE_INFO['ADDRESS_COUNTRY'], self.DATA_USERS['Country_address'])

        self.fill_text_field(self.EMPLOYEE_INFO['DESCRIPTION'], self.DATA_USERS['description'])

        self.fill_text_field(self.EMPLOYEE_INFO['EMAIL'], self.EMAIL)
