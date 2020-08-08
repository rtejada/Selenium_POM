from lib.suitecrm_base_page import SuitecrmBasePage
from selenium.webdriver.common.by import By


class SearchCase(SuitecrmBasePage):

    VIEW_CASES = (By.LINK_TEXT, 'Ver Casos')
    FILTER = (By.XPATH, "//a[@title = 'Filtro']")
    RAPID_FILTER = (By.LINK_TEXT, 'Filtro rápido')
    WINDOW_VISIBLE = (By.ID, 'searchDialog')
    BUTTON_NAME = (By.ID, 'name_basic')
    SEARCH = (By.ID, 'search_form_submit')

    def search_user(self, user):

        self.click_button(self.VIEW_CASES)

        self.wait_selector_visible(self.FILTER)

        self.click_button(self.FILTER)

        self.wait_selector_visible(self.WINDOW_VISIBLE)

        self.click_button(self.RAPID_FILTER)

        self.wait_selector_visible(self.BUTTON_NAME)

        self.fill_text_field(self.BUTTON_NAME, user)

        self.send_enter_key(self.SEARCH)

        '''
        self.wait_selector_visible(self.press_filter)

        self.click_button(self.press_filter)

        self.wait_selector_visible(self.wait_window_visible)

        self.click_button(self.press_quick_filter)

        self.wait_selector_visible(self.selector_search_field)

        self.fill_text_field(self.selector_search_field, user)

        self.send_enter_key(self.search_query)

        rows = len(self.driver.find_elements(By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr'))
        col = len(self.driver.find_elements(By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr/td'))
        for a in range(2, rows + 1):
            for b in range(1, col + 1):
                values = self.driver.find_element(By.XPATH,
                                                  '// *[@id = "MassUpdate"]/div[3]/table/tbody/tr[' + str(a) + ']/td[' + str(b) + ']/b/a')
                self.list_names.append(values.text)
        '''

        rows = len(self.driver.find_elements(By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr/td'))
        print(rows)

        self.click_button((By.LINK_TEXT, user))

        if rows >= 1:
            return True
        else:
            return False