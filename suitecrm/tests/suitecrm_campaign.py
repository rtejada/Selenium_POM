import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_campaign import CreateNewCampaign
from pages.configure_email import ConfigureEmail
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

        create_email = ConfigureEmail(self.driver)
        create_email.access_campaign_all()
        create_email.configure_email()

        create_campaign = CreateNewCampaign(self.driver)
        create_campaign.access_to_all()
        create_campaign.create_new_campaign()
        time.sleep(1)