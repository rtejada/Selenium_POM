import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_case import CreateCases
from lib.suitecrm_open_chrome_driver import *


class SuiteCrm(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.close()

    #def test_suitecrm(self):
    def suitecrm(self):
        auth_basic = AuthBasicPage(self.driver)
        auth_basic.authenticate()

        login = LoginPage(self.driver)
        login.login_user()

        cases = CreateCases(self.driver)
        cases.access_case()
        title_object = cases.new_case()
        found = cases.search_case(title_object)

        self.assertTrue(found, 'El Caso ' + title_object + ', no se ha creado')
