from selenium.webdriver.common.by import By
from lib.ip import IP
from lib.pages.cemip_base_page import CualEsMiIpBasePage
import os


class CualEsMiIpMaxMind(CualEsMiIpBasePage):

    URL = ''
    LOCATOR_WAIT = ''
    LOCATOR_COLUMN = ''

    def load_variables(self):
        self.URL = os.getenv("URL_MAXMIND")
        self.LOCATOR_WAIT = (By.XPATH, '//*[@id="geoip-demo-results-tbody"]/tr/td[1]')
        self.LOCATOR_COLUMN = (By.XPATH, '//*[@id="geoip-demo-results-tbody"]/tr/td')

    def __init__(self, driver):
        super().__init__(driver)
        self.load_variables()

    def get_data(self):

        col_maxmind = len(self.driver.find_elements(*self.LOCATOR_COLUMN))
        data_maxmind = []

        for j in range(1, col_maxmind):
            values = self.driver.find_element(By.XPATH,
                                              '//*[@id="geoip-demo-results-tbody"]/tr[' + str(1) + ']/td[' + str(j) + ']')
            data_maxmind.append(values.text)

        ip = IP()
        ip.ip = data_maxmind[0]

        city_nation = data_maxmind[2]
        ip.country = city_nation[26:31]
        ip.city = self.normalize(city_nation[0:8])
        longitude_latitude = data_maxmind[5]
        ip.lat = float(longitude_latitude[0:7])
        ip.lon = float(longitude_latitude[-7:])

        ip.isp = data_maxmind[7]

        return ip
