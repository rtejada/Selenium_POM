import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_budget import CreateNewBudget
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

        create_budget = CreateNewBudget(self.driver)
        create_budget.create_new_budget()
        title_budget = create_budget.get_title()
        found = create_budget.search_budget(title_budget)

        self.assertTrue(found, 'El Presupuesto no ha sido creado')

