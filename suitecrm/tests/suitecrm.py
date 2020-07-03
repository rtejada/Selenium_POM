import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_new_contact import CreateNewContact
from pages.suitecrm_create_customer_account import CreateCustomerAccount
from pages.suitecrm_assign_contact_customer_account import AssignContactCustomerAccount
from dotenv import load_dotenv
import time


class Suitecrm(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)
        load_dotenv()

    def tearDown(self):
        self.driver.close()

    def test_suitecrm(self):
        auth_basic = AuthBasicPage(self.driver)
        auth_basic.authenticate()

        login = LoginPage(self.driver)
        login.login_user()

        create_contact = CreateNewContact(self.driver)
        create_contact.page_contact()
        create_contact.create_new_contact()

        customer_account = CreateCustomerAccount(self.driver)
        customer_account.page_account()
        customer_account.create_customer_account()

        assign_customer_account = AssignContactCustomerAccount(self.driver)
        assign_customer_account.assign_contact()

        time.sleep(2)


