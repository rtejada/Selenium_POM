import unittest
from pages.suitecrm_auth_basic import AuthBasicPage
from pages.suitecrm_login_page import LoginPage
from pages.suitecrm_create_meeting import CreateNewMeeting
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

        meeting = CreateNewMeeting(self.driver)
        meeting.create()
        subject = meeting.get_meeting()
        found = meeting.search_meeting(subject)

        self.assertTrue(found, 'La Reunion no ha sido creada')

