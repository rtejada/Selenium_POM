from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
import json
from random import randint
import os


class CreateCampaignTemplates(SuitecrmBasePage):
    DATA_CAMPAIGN = ''

    RADIO_BUTTON = (By.ID, 'template_option_copy')
    NAME_TEMPLATE = (By.ID, 'template_id')
    SAVE = (By.ID, 'LBL_CREATE_EMAIL_TEMPLATE_BTN')
    CREATE_NEW_TRACK = (By.ID, 'LBL_CREATE_TRACKER_BTN')
    NEXT = 'wiz_next_button'
    BUTTON_NEXT = (By.ID, NEXT)
    WINDOW_VISIBLE = (By.ID, 'templateManagerDialog')
    TEXT_LINK = (By.ID, 'url_text')
    TRACKER_URL_ADD = (By.ID, 'tracker_url_add')
    SAVE_NEW_TRACK = (By.ID, 'templateManagerActionOK')
    SELECT_FILE = (By.ID, 'email_attachment0')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/data/data_campaign.json") as file:
            self.DATA_CAMPAIGN = json.load(file)

        self.DATA_CAMPAIGN['text_link'] = self.DATA_CAMPAIGN['text_link'] + str(randint(222, 9999)) + ' '

    def create_templates(self):

        radio = self.driver.find_element(*self.RADIO_BUTTON)
        radio.click()

        self.fill_select_by_text(self.NAME_TEMPLATE, self.DATA_CAMPAIGN['template_name'])

        self.send_enter_key(self.SAVE)

        self.click_button(self.CREATE_NEW_TRACK)

        self.wait_selector_visible(self.WINDOW_VISIBLE)

        self.fill_text_field(self.TEXT_LINK, self.DATA_CAMPAIGN['text_link'])

        self.fill_text_field(self.TRACKER_URL_ADD, self.DATA_CAMPAIGN['url_traceability'])

        self.click_button(self.SAVE_NEW_TRACK)

        file_add = self.driver.find_element(*self.SELECT_FILE)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_add)
        file_add.send_keys(os.getenv("DATA_PATH")+'imagen.png')

        self.window_scroll_home()

        self.wait_button_clickable(self.BUTTON_NEXT)

        self.click_by_javascript(self.NEXT)

