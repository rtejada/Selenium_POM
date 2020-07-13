from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
import json
from random import randint


class CreateCampaignTemplates(SuitecrmBasePage):
    DATA_CAMPAIGN = ''

    RADIO_BUTTON = (By.ID, 'template_option_copy')
    NAME_TEMPLATE = (By.ID, 'template_id')
    SAVE = (By.ID, 'LBL_SAVE_EMAIL_TEMPLATE_BTN')
    CREATE_NEW_TRACK = (By.ID, 'LBL_CREATE_TRACKER_BTN')
    BUTTON_NEXT = (By.ID, 'wiz_next_button')
    WINDOW_VISIBLE = (By.ID, 'templateManagerDialog')
    TEXT_LINK = (By.ID, 'url_text')
    TRACKER_URL_ADD = (By.ID, 'tracker_url_add')
    SAVE_NEW_TRACK = (By.ID, 'templateManagerActionOK')
    SELECT_FILE = (By.ID, 'email_attachment0')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_campaign.json") as file:
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

        self.window_scroll()

        file_add = self.driver.find_element(self.SELECT_FILE)
        file_add.send_keys("../data/image.png")

        self.window_scroll_home()

        self.click_button(self.BUTTON_NEXT)

