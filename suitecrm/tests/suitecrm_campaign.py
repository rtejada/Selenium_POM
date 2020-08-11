import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_campaign import CreateCampaign
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

        campaign = CreateCampaign(self.driver)
        email_name, sender_address, email_server = campaign.configure_email()
        name_campaign = campaign.campaign_header()
        campaign.campaign_target_list()
        campaign.campaign_templates()
        campaign.campaign_email_marketing(email_name, sender_address, email_server)
        found = campaign.search_campaign(name_campaign)

        self.assertTrue(found, 'La campaña' + name_campaign + 'no se ha creado')








