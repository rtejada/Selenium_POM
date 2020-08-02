from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
import json
from random import randint
import time


class CreateCampaignTargetGroupList(SuitecrmBasePage):
    DATA_CAMPAIGN = ''

    NEW_TARGET_LIST = (By.ID, 'target_list_name')
    BUTTON_CREATE_TARGET = (By.XPATH, "//*[@id='step2']//div/input[@value='Crear']")
    TYPE_LIST = (By.ID, 'target_list_type')
    RADIO_BUTTON = (By.ID, 'templateManager')
    NAME_TEMPLATE = (By.ID, 'template_id')
    SAVE = (By.ID, 'LBL_SAVE_EMAIL_TEMPLATE_BTN')
    BUTTON_NEXT = (By.ID, 'wiz_submit_button')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_campaign.json") as file:
            self.DATA_CAMPAIGN = json.load(file)

        self.DATA_CAMPAIGN['target_list_name'] = self.DATA_CAMPAIGN['target_list_name'] + str(randint(1, 50000))

    def create_target_group_list(self):

        self.fill_text_field(self.NEW_TARGET_LIST, self.DATA_CAMPAIGN['target_list_name'])

        self.fill_select_field(self.TYPE_LIST, self.DATA_CAMPAIGN['type'])

        self.click_button(self.BUTTON_CREATE_TARGET)

        time.sleep(3)

        self.click_button(self.BUTTON_NEXT)


