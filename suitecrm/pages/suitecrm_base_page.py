from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SuitecrmBasePage:

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.driver = driver
        """:type: Chrome"""

    def fill_select_field(self, selector, text):
        element_select = self.driver.find_element(*selector)
        type_select = Select(element_select)
        type_select.select_by_value(text)

    def fill_select_by_text(self, selector, text):
        element_select = self.driver.find_element(*selector)
        type_select = Select(element_select)
        type_select.select_by_visible_text(text)

    def fill_text_field(self, selector, text):
        element = self.driver.find_element(*selector)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_button(self, selector):
        element = self.driver.find_element(*selector)
        element.click()


    def send_enter_key(self, selector):
        save = self.driver.find_element(*selector)
        save.send_keys(Keys.ENTER)

    def menu_select_option(self, menu_selector, option_selector):

        select_button = self.driver.find_element(*menu_selector)
        select_button.click()

        action = ActionChains(self.driver)
        action.move_to_element(select_button).perform()

        self.wait_button_clickable(option_selector)

        access_option_selector = self.driver.find_element(*option_selector)
        action.move_to_element(access_option_selector)
        action.click()
        action.perform()

    def wait_button_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(locator))

    def wait_selector_visible(self, locator):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(locator))

    def window_scroll(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    def window_scroll_half(self):
        #Si quieres bajar a algún nivel, usa esto, aquí he usado "1000", puedes variar según tu uso#

        self.driver.execute_script("scrollBy(0,+500);")

    def window_scroll_home(self):
        #Si quieres subir de nivel, usa esto, otra vez usé aquí "-500", puedes variar según su uso..

        self.driver.execute_script("scrollBy(0,-500);")



