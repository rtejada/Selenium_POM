from lib.login import Login
from lib.pages.realworld_base_page import RealworldCounduitBasePage
import os


class RealworldHome(RealworldCounduitBasePage):

    URL = ''

    def load_variables(self):

        self.URL = os.getenv("URL")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

    def init_session(self):
        login = Login(self.driver)
        url_profile = login.login_user()
        return url_profile

