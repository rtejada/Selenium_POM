from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.realworld_base_page import RealworldCounduitBasePage


class AddComment(RealworldCounduitBasePage):

    COMMENT = 'Este es un comentario simple'
    BUTTON_WAIT_LOCATOR_ONE = (By.XPATH, '//*[@id="main"]//div[1]/a/h1')
    BUTTON_WAIT_LOCATOR_THREE = (By.XPATH, "//div/p[@class='card-text']")
    BUTTON_WAIT_LOCATOR_TWO = (By.XPATH, "//div/form/div/textarea[@class='form-control']")
    GO_COMMENT = '//*[@id="main"]//div[1]/a/h1'
    ADD_COMMENT = "//div/form/div/textarea[@class='form-control']"
    BUTTON_SENT_COMMENT = "//div/button[@type='submit']"
    GET_COMMENT = "//div/p[@class='card-text']"

    def wait_button_one(self):
        self.wait_selector_clickable(self.BUTTON_WAIT_LOCATOR_ONE)

    def search_button_comment(self):
        go_comment = self.driver.find_element_by_xpath(self.GO_COMMENT)
        go_comment.click()

    def wait_button_two(self):
        self.wait_selector_visible(self.BUTTON_WAIT_LOCATOR_TWO)

    def add_comment(self):
        add_comment = self.driver.find_element_by_xpath(self.ADD_COMMENT)
        add_comment.click()

        add_comment.send_keys(self.COMMENT)
        sent_comment = self.driver.find_element_by_xpath(self.BUTTON_SENT_COMMENT)
        sent_comment.send_keys(Keys.ENTER)

    def wait_button_three(self):
        self.wait_selector_visible(self.BUTTON_WAIT_LOCATOR_THREE)

    def get_comment(self):
        get_comment = self.driver.find_element_by_xpath(self.GET_COMMENT)
        get_comment = get_comment.text
        return get_comment, self.COMMENT

