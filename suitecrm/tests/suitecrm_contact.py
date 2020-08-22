import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_contact import CreateContact
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

        contact = CreateContact(self.driver)
        contact.page_contact()
        email, complete_name = contact.create_contact()

        found = contact.search_contact(complete_name)

        self.assertTrue(found, 'El Contacto ' + complete_name + ', no se ha creado')






        










