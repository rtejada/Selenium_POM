from lib.login import Login
from pages.realworld_base_page import RealworldCounduitBasePage


class RealworldHome(RealworldCounduitBasePage):

    URL = 'https://react-redux.realworld.io/'

    def init_session(self):
        login = Login(self.driver)
        url_profile = login.login_user()
        return url_profile


