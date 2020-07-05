from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class SuitecrmBasePage:

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.driver = driver
        """:type: Chrome"""

    def fill_select_field(self, selector, text):
        element_select = self.driver.find_element(*selector)
        type_select = Select(element_select)
        type_select.select_by_value(text)

    def fill_text_field(self, selector, text):
        element = self.driver.find_element(*selector)
        element.click()
        element.send_keys(text)

    def click_button(self, selector):
        element_copy = self.driver.find_element(*selector)
        element_copy.click()

    def button_save(self, selector):
        save = self.driver.find_element(*selector)
        save.send_keys(Keys.ENTER)

    def window_scroll(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')





