from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RealworldCounduitBasePage:
    URL = ''
    WAIT_LOCATOR = ''

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def wait_selector_clickable(self, locator=WAIT_LOCATOR):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(locator))

    def wait_selector_visible(self, locator=WAIT_LOCATOR):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(locator))

    def fill_field(self, selector, text):
        element = self.driver.find_element(selector)
        element.click()
        element.send_keys(text)

