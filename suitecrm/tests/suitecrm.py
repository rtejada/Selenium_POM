import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_new_contact import CreateNewContact
from pages.suitecrm_create_customer_account import CreateCustomerAccount
from pages.suitecrm_assign_contact_customer_account import AssignContactCustomerAccount
from pages.suitecrm_search_customer import SearchCustomer
from pages.suitecrm_search_contact import SearchContact
from dotenv import load_dotenv


class Suitecrm(unittest.TestCase):

    def setUp(self):
        options = Options()
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

        create_contact = CreateNewContact(self.driver)
        create_contact.page_contact()
        create_contact.create_new_contact()

        contact_email = create_contact.get_contact_email()
        contact_name = create_contact.get_contact_name()

        customer_account = CreateCustomerAccount(self.driver)
        customer_account.page_account()
        customer_account.create_customer_account()

        customer_email = customer_account.get_customer_email()
        customer_name = customer_account.get_customer_name()

        assign_customer_account = AssignContactCustomerAccount(self.driver)
        assign_customer_account.assign_contact(contact_email, contact_name)

        search_contact = SearchContact(self.driver)
        search_contact.search_contact(contact_email, contact_name)









