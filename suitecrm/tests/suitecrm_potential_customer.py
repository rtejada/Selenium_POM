import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_potential_customer import PotentialCustomer
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

        potential_customer = PotentialCustomer(self.driver)
        potential_customer.page_account()
        name = potential_customer.create()
        found = potential_customer.search(name)

        self.assertTrue(found, 'El cliente Potencial, no ha sido creado')


