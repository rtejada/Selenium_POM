from selenium import webdriver
from selenium.webdriver.common.by import By


class SuitecrmSiteSearch:

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.window_before = ''
        self.driver = driver
        """:type: Chrome"""

    def open_site_search(self, selector):
        search = self.driver.find_element(*selector)
        self.window_before = self.driver.window_handles[0]
        search.click()

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def search_for_name(self, selector, text):
        element = self.driver.find_element(*selector)
        element.click()
        element.clear()
        element.send_keys(text)

        click_name = self.driver.find_element(By.LINK_TEXT, text)
        click_name.click()



    '''
    search = self.driver.find_element(*self.SEARCH_ACCOUNT)
        window_before = self.driver.window_handles[0]
        search.click()

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        self.fill_text_field(self.SEARCH_FOR_NAME, self.CUSTOMER)

        self.click_button(self.SEARCH_BUTTON)

        click_name = self.driver.find_element(By.LINK_TEXT, self.CUSTOMER)
        click_name.click()

        self.driver.switch_to.window(window_before)
        '''