from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from random import randint
import json


class CreateCampaignHeader(SuitecrmBasePage):
    DATA_CAMPAIGN = ''

    BUTTON_ALL = (By.LINK_TEXT, 'TODO')
    ACCESS_CAMPAIGN = (By.LINK_TEXT, 'Campañas')
    CREATE_CAMPAIGN = (By.LINK_TEXT, 'Crear Campaña')
    TYPE_CAMPAIGN = (By.LINK_TEXT, 'Email')
    NAME_CAMPAIGN = (By.ID, 'name')
    DESCRIPTION = (By.ID, 'wiz_content')
    STATUS = (By.ID, 'status')
    QUOTE = (By.ID, 'budget')
    ACTUAL_COST = (By.ID, 'actual_cost')
    EXPECTED_REVENUE = (By.ID, 'expected_revenue')
    EXPECTED_COST = (By.ID, 'expected_cost')
    IMPRESSIONS = (By.ID, 'impressions')
    OBJECTIVE = (By.ID, 'objective')
    BUTTON_NEXT = (By.ID, 'wiz_next_button')

    def __init__(self, driver):
        super().__init__(driver)

        with open("../data/data_campaign.json") as file:
            self.DATA_CAMPAIGN = json.load(file)
            
        self.DATA_CAMPAIGN['name_campaign'] = self.DATA_CAMPAIGN['name_campaign'] + ' ' + str(randint(1, 90000000))
        self.DATA_CAMPAIGN['target_list_name'] = self.DATA_CAMPAIGN['target_list_name'] + ' ' + str(randint(1, 90000000))
        self.DATA_CAMPAIGN['name_marketing'] = self.DATA_CAMPAIGN['name_marketing'] + ' ' + str(randint(1, 90000000))

    def create_campaign_header(self):

        self.click_button(self.CREATE_CAMPAIGN)

        self.click_button(self.TYPE_CAMPAIGN)

        self.fill_text_field(self.NAME_CAMPAIGN, self.DATA_CAMPAIGN['name_campaign'])

        self.fill_select_field(self.STATUS, self.DATA_CAMPAIGN['status'])

        self.fill_text_field(self.DESCRIPTION, self.DATA_CAMPAIGN['description'])

        self.window_scroll_half()

        self.wait_selector_visible(self.QUOTE)

        self.fill_text_field(self.QUOTE, self.DATA_CAMPAIGN['quote'])

        self.fill_text_field(self.ACTUAL_COST, self.DATA_CAMPAIGN['actual_cost'])

        self.fill_text_field(self.EXPECTED_REVENUE, self.DATA_CAMPAIGN['expected_revenue'])

        self.fill_text_field(self.EXPECTED_COST, self.DATA_CAMPAIGN['expected_cost'])

        self.fill_text_field(self.IMPRESSIONS, self.DATA_CAMPAIGN['impressions'])

        self.fill_text_field(self.OBJECTIVE, self.DATA_CAMPAIGN['objective'])

        self.window_scroll_home()

        self.click_button(self.BUTTON_NEXT)

        return self.DATA_CAMPAIGN['name_campaign']













