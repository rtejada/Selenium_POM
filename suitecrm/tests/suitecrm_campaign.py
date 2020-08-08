import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_campaign_header import CreateCampaignHeader
from pages.suitecrm_camp_create_templates import CreateCampaignTemplates
from pages.suitecrm_camp_target_group_lists import CreateCampaignTargetGroupList
from pages.suitecrm_camp_number_email_marketing import CreateCampaignEmailMarketing
from pages.suitecrm_configure_email import ConfigureEmail
from dotenv import load_dotenv


class SuiteCrm(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        load_dotenv()

    def tearDown(self):
        self.driver.close()

    def test_suitecrm(self):
        auth_basic = AuthBasicPage(self.driver)
        auth_basic.authenticate()

        login = LoginPage(self.driver)
        login.login_user()

        config_email = ConfigureEmail(self.driver)
        config_email.access_campaign_all()
        email_name, sender_address, email_server = config_email.configure_email()

        create_campaign_header = CreateCampaignHeader(self.driver)
        name_campaign = create_campaign_header.create_campaign_header()

        create_camp_target_list = CreateCampaignTargetGroupList(self.driver)
        create_camp_target_list.create_target_group_list()

        create_camp_templates = CreateCampaignTemplates(self.driver)
        create_camp_templates.create_templates()

        create_number_email_marketing = CreateCampaignEmailMarketing(self.driver)
        create_number_email_marketing.create_marketing_email(email_name, sender_address, email_server)








