from selenium import webdriver
from selenium.webdriver import Chrome


class SuitecrmBasePage:

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.driver = driver
        """:type: Chrome"""



