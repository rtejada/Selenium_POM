from selenium.webdriver.common.by import By
from lib.suitecrm_base_page import SuitecrmBasePage

class SuitecrmSiteSearch(SuitecrmBasePage):

    access_menu = ''
    press_filter = ''
    table_rows_selector = ''
    name_user = ''
    wait_window_visible = ''
    selector_search_field = ''
    search_query = ''
    list_names = []

    def search_element(self, user):

        self.click_button(self.access_menu)

        self.wait_selector_visible(self.press_filter)

        rows_count = len(self.driver.find_elements(self.table_rows_selector))
        #col = len(self.driver.find_elements(By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr/td'))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element(self.name_user + 'tr[' + str(a) + ']/td[3]//a')
            self.list_names.append(value.text)

        if user in self.list_names:
            return True
        else:
            return False

