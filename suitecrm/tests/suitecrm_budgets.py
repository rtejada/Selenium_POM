import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_budget import CreateNewBudget


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

        create_budget = CreateNewBudget(self.driver)
        create_budget.create()
