from lib.suitecrm_base_page import SuitecrmBasePage
from lib.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By
from random import randint
import json


class CreateNewMeeting(SuitecrmBasePage):
    
    LIST_MEETING = ''
    BUTTON_ALL = (By.LINK_TEXT, 'TODO')
    MEETING = (By.LINK_TEXT, 'Reuniones')
    SCHEDULE_MEETING = (By.LINK_TEXT, 'Programar Reunión')
    SUBJECT = (By.ID, 'name')

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

        with open("../data/data_users.json") as file:
            self.LIST_MEETING = json.load(file)

        self.LIST_MEETING['subject'] = self.LIST_MEETING['subject'] + str(randint(500, 1000))

        self.LIST_MEETING['target_list_name'] = self.LIST_MEETING['target_list_name'] + ' ' + str(
            randint(1, 90000000))
        self.LIST_MEETING['name_marketing'] = self.LIST_MEETING['name_marketing'] + ' ' + str(randint(1, 90000000))

    def create(self):

        self.menu_select_option(self.BUTTON_ALL, self.MEETING)

        self.wait_selector_visible(self.SCHEDULE_MEETING)

        self.click_button(self.SCHEDULE_MEETING)

        