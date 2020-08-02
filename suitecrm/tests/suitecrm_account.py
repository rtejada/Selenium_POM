import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_customer_account import CreateCustomerAccount
from lib.suitecrm_search_customer import SearchCustomer

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

        customer_account = CreateCustomerAccount(self.driver)
        customer_account.page_account()
        customer_account.create_customer_account()

        customer_name = customer_account.get_customer_name()

        search_customer = SearchCustomer(self.driver)
        customer = search_customer.search_customer(customer_name)

        self.assertEqual(customer_name, customer)