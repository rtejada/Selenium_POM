from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cemip_base_page import CualEsMiIpBasePage

import os


class CualEsMiIpHome(CualEsMiIpBasePage):

    URL = ''
    LINK_TEXT_BUTTON = ''
    LOCATOR_WAIT = ''

    def load_variables(self):

        self.URL = os.getenv("URL_CEMIP")
        self.LINK_TEXT_BUTTON = 'Geolocalizar IP'
        self.LOCATOR_WAIT = (By.ID, "direccion-ip")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

    def press_button(self):
        geolocate_button = self.driver.find_element_by_link_text(self.LINK_TEXT_BUTTON)
        geolocate_button.send_keys(Keys.RETURN)

