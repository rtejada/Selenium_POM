import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_user_profile import FillUserProfile
from pages.suitecrm_create_user import CreateUser


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

        create_user = CreateUser(self.driver)
        create_user.select_menu()
        user_name, complete_name = create_user.fill_user_profile()
        create_user.fill_employee_info()
        create_user.save()

        print(user_name, ' ', complete_name)
