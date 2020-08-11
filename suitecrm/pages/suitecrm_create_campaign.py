from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage
from pages.suitecrm_campaign_header import CreateCampaignHeader
from pages.suitecrm_campaign_templates import CreateCampaignTemplates
from pages.suitecrm_camp_target_group_lists import CreateCampaignTargetGroupList
from pages.suitecrm_camp_number_email_marketing import CreateCampaignEmailMarketing
from lib.suitecrm_search_options_window import SuitecrmSiteSearchElement
from pages.suitecrm_configure_email import ConfigureEmail


class CreateCampaign(SuitecrmBasePage):

    VIEW_CAMPAIGN = (By.LINK_TEXT, 'Ver Campañas')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr')
    NAME_SELECTOR = '//*[@id = "MassUpdate"]//div/table/tbody/'
    COL_SELECTOR = '/td[3]//a'

    def configure_email(self):

        config_email = ConfigureEmail(self.driver)
        config_email.access_campaign_all()
        email_name, sender_address, email_server = config_email.configure_email()

        return email_name, sender_address, email_server

    def campaign_header(self):

        create_campaign_header = CreateCampaignHeader(self.driver)
        create_campaign_header.create_campaign_header()
        name_campaign = create_campaign_header.get_campaign()

        return name_campaign

    def campaign_target_list(self):

        create_camp_target_list = CreateCampaignTargetGroupList(self.driver)
        create_camp_target_list.create_target_group_list()

    def campaign_templates(self):

        create_camp_templates = CreateCampaignTemplates(self.driver)
        create_camp_templates.create_templates()

    def campaign_email_marketing(self, email_name, sender_address, email_server):

        create_number_email_marketing = CreateCampaignEmailMarketing(self.driver)
        create_number_email_marketing.create_marketing_email(email_name, sender_address, email_server)

    def search_campaign(self, name_campaign):

        search_contact = SuitecrmSiteSearchElement(self.driver)
        search_contact.access_option = self.VIEW_CAMPAIGN
        search_contact.press_filter = self.FILTER
        search_contact.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_contact.col_selector = self.COL_SELECTOR
        search_contact.name_selector = self.NAME_SELECTOR
        value = search_contact.search_element(name_campaign)

        return value
