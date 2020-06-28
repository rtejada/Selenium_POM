from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserProfile:

    PAGE_PROFILE_USER = '//*[@id="main"]//div/ul/li[4]/a'
    BUTTON_WAIT_LOCATOR = (By.XPATH, '//*[@id="main"]//div[1]/a/h1')
    LAST_PUBLISHED_ARTICLE = '//*[@id="main"]//div[1]/a/h1'

    def __init__(self, driver):
        self.driver = driver

    def open_window_one(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        profile = self.driver.find_element_by_xpath(self.PAGE_PROFILE_USER)
        profile.click()

    def wait_button(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(self.BUTTON_WAIT_LOCATOR))

    def last_published(self):

        last_published_article = self.driver.find_element_by_xpath(self.LAST_PUBLISHED_ARTICLE)
        last_published_article = last_published_article.text

        return last_published_article
