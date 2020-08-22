import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_opportunity import CreateOpportunity
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

        create_opportunity = CreateOpportunity(self.driver)
        create_opportunity.access()
        name_opportunity = create_opportunity.create()
        found = create_opportunity.search(name_opportunity)

        self.assertTrue(found, 'La Oportunidad no se ha creado')



