import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_campaign import CreateNewCampaign
from pages.suitecrm_configure_email import ConfigureEmail
from dotenv import load_dotenv
import time


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

        configure_email = ConfigureEmail(self.driver)
        configure_email.access_campaign_all()
        email_name, sender_address, email_server = configure_email.configure_email()

        create_campaign = CreateNewCampaign(self.driver)
        create_campaign.create_new_campaign()
        create_campaign.create_new_target_list()
        create_campaign.create_marketing_email(email_name, sender_address, email_server)
