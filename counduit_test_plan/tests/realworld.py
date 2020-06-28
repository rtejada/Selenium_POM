import unittest
from selenium import webdriver
from pages.realworld_home import RealworldHome
from pages.realworld_post import RealworldPost
from pages.realworld_confirm_post import PostPage
from pages.realworld_user_profile import UserProfile
from pages.realworld_add_comment import AddComment


class Realworld(unittest.TestCase):

    def setUp(self):
        #options = Options()
        #options.add_argument("--incognito")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_realworld_page(self):

        home = RealworldHome(self.driver)
        home.load()
        home.init_session()

        post = RealworldPost(self.driver)
        post.wait_button()
        title_article, body_article = post.register_new_post()
        post_url = post.get_url()

        confirm_post = PostPage(self.driver)
        confirm_post.open_window_of_post(post_url)
        confirm_post.wait_button()
        title, body = confirm_post.data_test()

        self.assertEqual(title_article, title)
        self.assertEqual(body_article, body)

        profile = UserProfile(self.driver)
        profile.open_window_one()
        profile.wait_button()
        last_published_article = profile.last_published()

        self.assertEqual(title_article, last_published_article)

        add = AddComment(self.driver)
        add.wait_button_one()
        add.search_button_comment()
        add.wait_button_two()
        add.add_comment()
        add.wait_button_three()
        get_comment, comment = add.get_comment()
        self.assertEqual(get_comment, comment)

