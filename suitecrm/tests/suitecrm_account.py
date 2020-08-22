import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_customer_account import CustomerAccount

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

        customer_account = CustomerAccount(self.driver)
        customer_account.page_account()
        email, account = customer_account.create_customer_account()

        found = customer_account.search_customer(account)

        self.assertTrue(found, 'La cuenta ' + account + ', no se ha creado')





