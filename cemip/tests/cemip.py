import unittest

from selenium import webdriver
from pages.cemip_geo import CualEsMiIpGeo
from pages.cemip_home import CualEsMiIpHome
from pages.cemip_maxmind import CualEsMiIpMaxMind
from dotenv import load_dotenv

class CemipPOM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        load_dotenv()


    def tearDown(self):
        self.driver.close()

    def test_cemip(self):
        
        home = CualEsMiIpHome(self.driver)
        
        home.load()
        home.press_button()
        home.wait_element_visible()
        
        geo = CualEsMiIpGeo(self.driver)
        
        cemip_data = geo.get_data()
        
        maxm = CualEsMiIpMaxMind(self.driver)
        
        maxm.load()
        maxm.wait_element_visible()
        
        maxmip_data = maxm.get_data()

        self.assertEqual(cemip_data.ip, maxmip_data.ip)
        self.assertEqual(cemip_data.country, maxmip_data.country)
        self.assertEqual(cemip_data.city, maxmip_data.city)
        self.assertEqual(cemip_data.lat, maxmip_data.lat)
        self.assertEqual(cemip_data.lon, maxmip_data.lon)
        self.assertEqual(cemip_data.isp, maxmip_data.isp)


if __name__ == '__main__':
    unittest.main()
