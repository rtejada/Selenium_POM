from selenium.webdriver.common.by import By


class DuckDuckGoResultsPage(object):
    
    LINK_DIVS = (By.CSS_SELECTOR, '#links > div')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SELECTOR_RESULTS = (By.CSS_SELECTOR, "div.results_links_deep")

    def __init__(self, driver):
        self.driver = driver

    def link_div_count(self):
        link_divs = self.driver.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self):
        phrase_results = self.driver.find_elements(*self.SELECTOR_RESULTS)
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
