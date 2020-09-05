from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
import json
import os
from random import randint


class CreateNew(SuitecrmBasePage):

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_CONTACT = (By.LINK_TEXT, 'Crear Cuentas')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    PHONE_WORK = (By.ID, 'phone_work')
    PHONE_MOBILE = (By.ID, 'phone_mobile')
    PHONE_FAX = (By.ID, 'phone_fax')
    JOB_POSITION = (By.ID, 'title')
    DEPART = (By.ID, 'department')
    NAME_ACCOUNT = (By.ID, 'EditView_account_name')
    ADDRESS = (By.ID, 'primary_address_street')
    CITY = (By.ID, 'primary_address_city')
    ADDRESS_STATE = (By.ID, 'primary_address_state')
    WEB = (By.ID, 'website')
    EMAIL = (By.ID, 'Leads0emailAddress0')
    CP = (By.ID, 'primary_address_postalcode')
    COUNTRY = (By.ID, 'primary_address_country')
    BUTTON_COPY = (By.ID, 'alt_checkbox')
    WEB_SITE = (By.ID, 'website')
    DESCRIPTION = (By.ID, 'description')
    STATUS = (By.ID, 'status')
    STATUS_DESCRIPTION = (By.ID, 'status_description')
    LEAD_SOURCE = (By.ID, 'lead_source')
    LEAD_SOURCE_DESCRIPTION = (By.ID, 'lead_source_description')
    OPPORTUNITY_AMOUNT = (By.ID, 'opportunity_amount')
    REFERED_BY = (By.ID, 'refered_by')

    CAMPAIGN = (By.ID, 'btn_campaign_name')
    NAME = (By.ID, 'name_advanced')
    ASSIGNED_A = (By.ID, 'btn_assigned_user_name')
    LAST_NAME_ADVANCED = (By.ID, 'last_name_advanced')
    SAVE = (By.ID, 'SAVE')

    def __init__(self, driver):
        super().__init__(driver)
        
        with open(os.getcwd() + "/data/potential_customers.json") as file:
            self.LIST_POT_CUSTOM = json.load(file)

        self.FULL_NAME = self.LIST_POT_CUSTOM['full_name']
        self.first_name = self.FULL_NAME[0] + self.random_letter(5)
        self.last_name = self.FULL_NAME[1] + self.random_letter(5)
        self.job_position = self.LIST_POT_CUSTOM['job_position'] + ' ' + self.random_letter(7)
        self.phone_work = self.LIST_POT_CUSTOM['telephone'] + str(randint(1, 900000000000))
        self.phone_mobile = self.LIST_POT_CUSTOM['mobile'] + randint(1, 90000000000)
        self.phone_fax = self.LIST_POT_CUSTOM['fax'] + randint(1, 90000000000)
        self.web_site = self.LIST_POT_CUSTOM['web'] + self.random_letter(8) + '.es'
        self.email = self.LIST_POT_CUSTOM['email'] + self.random_letter(7) + '@' + self.random_letter(8) + '.com'
        self.name_potential_customer = self.first_name + ' ' + self.last_name

    def customer(self):

        self.fill_text_field(self.FIRST_NAME, self.first_name)

        self.fill_text_field(self.LAST_NAME, self.last_name)

        self.fill_text_field(self.PHONE_WORK, self.phone_work)

        self.fill_text_field(self.JOB_POSITION, self.job_position)

        self.fill_text_field(self.PHONE_MOBILE, self.phone_mobile)

        self.fill_text_field(self.DEPART, self.LIST_POT_CUSTOM['depart'])

        self.fill_text_field(self.PHONE_FAX, self.phone_fax)

        self.fill_text_field(self.NAME_ACCOUNT, self.LIST_POT_CUSTOM['name_account'])

        self.fill_text_field(self.WEB_SITE, self.web_site)

        self.fill_text_field(self.ADDRESS, self.LIST_POT_CUSTOM['address'])

        self.fill_text_field(self.CITY, self.LIST_POT_CUSTOM['city'])

        self.fill_text_field(self.ADDRESS_STATE, self.LIST_POT_CUSTOM['state'])

        self.fill_text_field(self.CP, self.LIST_POT_CUSTOM['cp'])

        self.fill_text_field(self.COUNTRY, self.LIST_POT_CUSTOM['country'])

        self.click_button(self.BUTTON_COPY)

        self.fill_text_field(self.EMAIL, self.email)

        self.fill_text_field(self.DESCRIPTION, self.LIST_POT_CUSTOM['description'])

        self.fill_select_field(self.STATUS, self.LIST_POT_CUSTOM['status'])

        self.fill_select_field(self.LEAD_SOURCE, self.LIST_POT_CUSTOM['lead_source'])

        self.fill_text_field(self.STATUS_DESCRIPTION, self.LIST_POT_CUSTOM['status_description'])

        self.fill_text_field(self.LEAD_SOURCE_DESCRIPTION, self.LIST_POT_CUSTOM['lead_source_description'])

        self.fill_text_field(self.OPPORTUNITY_AMOUNT, self.LIST_POT_CUSTOM['amount'])

        self.fill_text_field(self.REFERED_BY, self.LIST_POT_CUSTOM['refered_by'])

        find_data_campaign = SuitecrmSiteSearch(self.driver)
        find_data_campaign.selector_open_window = self.CAMPAIGN
        find_data_campaign.selector_search_field = self.NAME
        find_data_campaign.search_query = self.LIST_POT_CUSTOM['campaign']
        find_data_campaign.open_site_search()

        find_data_user = SuitecrmSiteSearch(self.driver)
        find_data_user.selector_open_window = self.ASSIGNED_A
        find_data_user.selector_search_field = self.LAST_NAME_ADVANCED
        find_data_user.search_query = self.LIST_POT_CUSTOM['user_last_name']
        find_data_user.open_site_search()

        self.send_enter_key(self.SAVE)

        return self.name_potential_customer













