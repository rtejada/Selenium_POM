from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CualEsMiIpBasePage:
    URL = ''
    BUTTON_WAIT_LOCATOR = ''
    LOCATOR_WAIT = ''

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def wait_element_visible(self):

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(self.LOCATOR_WAIT))