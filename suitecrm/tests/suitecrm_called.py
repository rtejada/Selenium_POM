import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_call import CreateCall
from lib.suitecrm_open_chrome_driver import *


class SuiteCrm(unittest.TestCase):

    def setUp(self):

        self.driver = get_driver()

    def test_suitecrm(self):
        auth_basic = AuthBasicPage(self.driver)
        auth_basic.authenticate()

        login = LoginPage(self.driver)
        login.login_user()

        called = CreateCall(self.driver)
        called.log_call()
        call_subject = called.get_call()
        found = called.search_call(call_subject)

        self.assertTrue(found, 'La Reunion no ha sido creada')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
