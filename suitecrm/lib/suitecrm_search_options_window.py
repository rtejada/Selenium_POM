from lib.suitecrm_base_page import SuitecrmBasePage


class SuitecrmSiteSearchElement(SuitecrmBasePage):

    access_option = ''
    press_filter = ''
    table_rows_selector = ''
    name_selector = ''
    col_selector = ''
    list_names = []

    def search_element(self, search_item):

        self.click_button(self.access_option)

        self.wait_selector_visible(self.press_filter)

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))
        #col = len(self.driver.find_elements(By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr/td'))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.name_selector + 'tr[' + str(a) + ']' + self.col_selector)

            self.list_names.append(value.text)

        if search_item in self.list_names:
            return True
        else:
            return False

