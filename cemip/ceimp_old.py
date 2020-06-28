import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GenerateMyIp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_access_page(self):
        self.driver.get('https://www.cual-es-mi-ip.net/')
        geolocate_button = self.driver.find_element_by_link_text('Geolocalizar IP')
        geolocate_button.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located((By.ID, "direccion-ip")))

        ip_address = self.driver.find_element(By.ID, 'direccion-ip')
        ip_ad = ip_address.get_attribute('value')

        rows = len(self.driver.find_elements(By.XPATH, '/html/body//div/table/tbody/tr'))
        col = len(self.driver.find_elements(By.XPATH, '/html/body//div/table/tbody/tr[1]/td'))
        data = []
        for a in range(1, rows + 1):
            for b in range(1, col + 1):
                values = self.driver.find_element(By.XPATH,
                                                  '/html/body//div/table/tbody/tr[' + str(a) + ']/td[' + str(b) + ']')
                data.append(values.text)

        print(data)

        self.driver.get('https://www.maxmind.com/en/locate-my-ip-address')
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="geoip-demo-results-tbody"]/tr/td[1]')))

        col_maxmind = len(self.driver.find_elements(By.XPATH, '//*[@id="geoip-demo-results-tbody"]/tr/td'))
        data_maxmind = []

        for j in range(1, col_maxmind):
            values = self.driver.find_element(By.XPATH,
                                              '//*[@id="geoip-demo-results-tbody"]/tr[' + str(1) + ']/td[' + str(j) + ']')
            data_maxmind.append(values.text)

        pais = data[1]
        ciudad = data[3]
        lat = float(data[5][0:8])
        latitud = round(lat, 4)
        lon = float(data[7][0:8])
        longitud = round(lon, 4)
        compania = data[9]

        ip = data_maxmind[0]
        city_nation = data_maxmind[2]
        nation = city_nation[26:31]
        city = city_nation[0:8]
        longitude_latitude = data_maxmind[5]
        latitude = float(longitude_latitude[0:7])
        longitude = float(longitude_latitude[-7:])
        company = data_maxmind[7]

        self.assertEqual(ip_ad, ip)
        self.assertEqual(pais, nation)
        self.assertEqual(ciudad, city)
        self.assertEqual(latitud, latitude)
        self.assertEqual(longitud, longitude)
        self.assertEqual(compania, company)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./MyIP'))

