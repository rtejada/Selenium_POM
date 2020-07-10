from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
from random import randint


class CreateNewCampaign(SuitecrmBasePage):

    CAMPAIGNS = {'name_campaign': 'Traime un Amigo', 'status': 'Active', 'description': 'Disponibles para clientes de Selenium'}
    QUOTE_CAMPAIGN = {'quote': '2000', 'actual_cost': '2500', 'expected_revenue': '5000', 'expected_cost': '3200',
                      'impressions': '7', 'objective': 'Conseguir rentabilidad', 'target_list_name': 'TA', 'type': 'test',
                      'template_name': 'Case Creation', 'marketing_name': 'Campaña ', 'hour_date': '25/07/2020',
                      'hour': '11', 'minute': '50', 'address_mail': 'Saint-Geniès-Bellevue@Toulose.fr'}

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
    NEW_TARGET_LIST = (By.ID, 'target_list_name')
    BUTTON_CREATE_TARGET = (By.XPATH, "//*[@id='step2']//div/input[@value='Crear']")
    TYPE_LIST = (By.ID, 'target_list_type')
    RADIO_BUTTON = (By.ID, 'template_option_copy')
    NAME_TEMPLATE = (By.ID, 'template_id')
    SAVE = (By.ID, 'LBL_SAVE_EMAIL_TEMPLATE_BTN')
    MARKETING_EMAIL = (By.ID, 'marketing_name')
    PROGRAM_HOUR_DATE = (By.ID, 'date_start_date')
    HOUR = (By.ID, 'date_start_hours')
    MINUTES = (By.ID, 'date_start_minutes')
    FROM_ADDRESS = (By.ID, 'from_addr')


    def __init__(self, driver):
        super().__init__(driver)
        self.CAMPAIGNS['name_campaign'] = self.CAMPAIGNS['name_campaign'] + ' ' + str(randint(1, 90000000))
        self.QUOTE_CAMPAIGN['target_list_name'] = self.QUOTE_CAMPAIGN['target_list_name'] + ' ' + str(randint(1, 90000000))
        self.QUOTE_CAMPAIGN['marketing_name'] = self.QUOTE_CAMPAIGN['marketing_name'] + ' ' + str(randint(1, 90000000))

    def access_to_all(self):

        self.menu_select_option(self.BUTTON_ALL, self.ACCESS_CAMPAIGN)

    def create_new_campaign(self):

        self.click_button(self.CREATE_CAMPAIGN)

        self.click_button(self.TYPE_CAMPAIGN)

        self.fill_text_field(self.NAME_CAMPAIGN, self.CAMPAIGNS['name_campaign'])

        self.fill_select_field(self.STATUS, self.CAMPAIGNS['status'])

        self.fill_text_field(self.DESCRIPTION, self.CAMPAIGNS['description'])

        self.window_scroll_half()

        self.wait_selector_visible(self.QUOTE)

        self.fill_text_field(self.QUOTE, self.QUOTE_CAMPAIGN['quote'])

        self.fill_text_field(self.ACTUAL_COST, self.QUOTE_CAMPAIGN['actual_cost'])

        self.fill_text_field(self.EXPECTED_REVENUE, self.QUOTE_CAMPAIGN['expected_revenue'])

        self.fill_text_field(self.EXPECTED_COST, self.QUOTE_CAMPAIGN['expected_cost'])

        self.fill_text_field(self.IMPRESSIONS, self.QUOTE_CAMPAIGN['impressions'])

        self.fill_text_field(self.OBJECTIVE, self.QUOTE_CAMPAIGN['objective'])

        self.window_scroll_home()

        self.click_button(self.BUTTON_NEXT)

    def create_new_target_list(self):

        self.fill_text_field(self.NEW_TARGET_LIST, self.QUOTE_CAMPAIGN['target_list_name'])

        self.fill_select_field(self.TYPE_LIST, self.QUOTE_CAMPAIGN['type'])

        self.click_button(self.BUTTON_CREATE_TARGET)

        self.click_button(self.BUTTON_NEXT)

    def create_templates(self):

        self.click_button(self.RADIO_BUTTON)

        self.fill_select_name(self.NAME_TEMPLATE, self.QUOTE_CAMPAIGN['template_name'])

        self.button(self.SAVE)

        self.wait_button_clickable(self.BUTTON_NEXT)

        self.click_button(self.BUTTON_NEXT)

    def create_marketing_email(self):

        self.fill_text_field(self.MARKETING_EMAIL, self.QUOTE_CAMPAIGN['marketing_name'])

        self.fill_text_field(self.PROGRAM_HOUR_DATE, self.QUOTE_CAMPAIGN['hour_date'])

        self.fill_select_field(self.HOUR, self.QUOTE_CAMPAIGN['hour'])

        self.fill_select_field(self.MINUTES, self.QUOTE_CAMPAIGN['minute'])

        self.fill_text_field(self.FROM_ADDRESS, self.QUOTE_CAMPAIGN['from_address'])

        self.window_scroll_home()

        self.click_button(self.BUTTON_NEXT)














