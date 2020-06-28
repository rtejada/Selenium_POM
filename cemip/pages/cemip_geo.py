
from selenium.webdriver.common.by import By
from pages.cemip_base_page import CualEsMiIpBasePage

from lib.ip import IP


class CualEsMiIpGeo(CualEsMiIpBasePage):

    LOCATOR_IP_ADDRESS = (By.ID, 'direccion-ip')
    LOCATOR_ROWS = (By.XPATH, '/html/body//div/table/tbody/tr')
    LOCATOR_COLS = (By.XPATH, '/html/body//div/table/tbody/tr[1]/td')

    def get_data(self):

        ip_address = self.driver.find_element(*self.LOCATOR_IP_ADDRESS)
        ip_addr = ip_address.get_attribute('value')

        rows = len(self.driver.find_elements(*self.LOCATOR_ROWS))
        col = len(self.driver.find_elements(*self.LOCATOR_COLS))

        data = []

        for a in range(1, rows + 1):
            for b in range(1, col + 1):
                values = self.driver.find_element(By.XPATH,
                                                  '/html/body//div/table/tbody/tr[' + str(a) + ']/td[' + str(b) + ']')
                data.append(values.text)

        ip = IP()

        ip.country = data[1]
        ip.city = data[3]

        lat = float(data[5][0:8])
        ip.lat = round(lat, 4)

        lon = float(data[7][0:8])
        ip.lon = round(lon, 4)

        ip.isp = data[9]
        ip.ip = ip_addr

        return ip

