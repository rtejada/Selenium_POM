from selenium.webdriver.common.by import By
from lib.pages.realworld_base_page import RealworldCounduitBasePage


class PostPage(RealworldCounduitBasePage):

    WAIT_LOCATOR = (By.XPATH, '//*[@id="main"]//div[1]/div/h1')
    TITLE_POST = '//*[@id="main"]//div[1]/div/h1'
    BODY_POST = '//*[@id="main"]//div[2]/div[1]//div/p'

    def open_window_of_post(self, url):

        self.driver.execute_script('window.open("");')

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)

    def wait_button(self):

        self.wait_selector_clickable(self.WAIT_LOCATOR)

    def data_test(self):

        title = self.driver.find_element_by_xpath(self.TITLE_POST)
        title = title.text

        body = self.driver.find_element_by_xpath(self.BODY_POST)
        body = body.text

        return title, body
