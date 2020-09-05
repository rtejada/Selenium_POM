from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
import json
import os
from random import randint


class CreateCampaignEmailMarketing(SuitecrmBasePage):

    DATA_CAMPAIGN = ''

    BUTTON_NEXT = (By.ID, 'wiz_submit_button')
    MARKETING_EMAIL = (By.ID, 'marketing_name')
    MARKETING_ACCOUNT = (By.ID, 'inbound_email_id')
    PROGRAM_HOUR_DATE = (By.ID, 'date_start_trigger')
    WINDOW_VISIBLE = (By.ID, 'date_start_trigger_div')
    DATE = (By.ID, 'date_start_trigger_div_t_cell21')
    HOUR = (By.ID, 'date_start_hours')
    MINUTES = (By.ID, 'date_start_minutes')
    FROM_NAME = (By.ID, 'from_name')
    FROM_ADDRESS = (By.ID, 'from_addr')
    NEW_WINDOWS = (By.ID, 'next_button_div')
    EMAIL_NAME = 'SUITE-CRM- 35337354'
    VISIBLE_LAUNCH_BUTTON = (By.XPATH, '//*[@id="step3"]//div//table/tbody/tr[3]/td/a')
    LAUNCH_EMAIL_SETTINGS = (By.LINK_TEXT, 'Lanzar Configuración de Email')
    SAVE = (By.ID, 'wiz_submit_button')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/data/data_campaign.json") as file:
            self.DATA_CAMPAIGN = json.load(file)

        self.DATA_CAMPAIGN['name_marketing'] = self.DATA_CAMPAIGN['name_marketing'] + str(randint(5000, 10000))

    def create_marketing_email(self, email_name, sender_address, email_server):

        self.wait_button_clickable(self.MARKETING_EMAIL)

        self.fill_text_field(self.MARKETING_EMAIL, self.DATA_CAMPAIGN['name_marketing'])

        self.fill_select_by_text(self.MARKETING_ACCOUNT, email_name)

        self.click_button(self.PROGRAM_HOUR_DATE)

        self.wait_selector_visible(self.WINDOW_VISIBLE)

        self.click_button(self.DATE)

        self.fill_text_field(self.FROM_NAME, sender_address)

        self.fill_text_field(self.FROM_ADDRESS, email_server)

        self.window_scroll_home()

        self.click_button(self.BUTTON_NEXT)

        self.wait_selector_visible(self.LAUNCH_EMAIL_SETTINGS)

        self.click_button(self.LAUNCH_EMAIL_SETTINGS)

        self.click_button(self.BUTTON_NEXT)


