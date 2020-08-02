import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_new_contact import CreateNewContact
from lib.suitecrm_search_contact import SearchContact

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

        create_contact = CreateNewContact(self.driver)
        create_contact.page_contact()
        create_contact.create_new_contact()

        contact_name = create_contact.get_contact_name()

        search_contact = SearchContact(self.driver)
        name = search_contact.search_contact(contact_name)

        self.assertEqual(contact_name, name)



        










