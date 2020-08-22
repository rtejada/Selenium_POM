import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_campaign import CreateCampaign

from lib.suitecrm_open_chrome_driver import *


class SuiteCrm(unittest.TestCase):

    def setUp(self):

        self.driver = get_driver()

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








