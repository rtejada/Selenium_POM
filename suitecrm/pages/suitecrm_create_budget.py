from pages.suitecrm_base_page import SuitecrmBasePage
from pages.suitecrm_site_search import SuitecrmSiteSearch
from selenium.webdriver.common.by import By

from random import randint
import csv


class CreateNewBudget(SuitecrmBasePage):

    BUDGETS = ''
    ACCESS_HOME = (By.LINK_TEXT, 'Todo')
    ACCESS_BUDGET = (By.LINK_TEXT, 'Presupuestos')
    CREATE_BUDGET = (By.LINK_TEXT, 'Crear')

    def __init__(self, driver):
        super().__init__(driver)

        file = open('bugets.csv')
        content = csv.reader(file, delimiter=',')
        self.BUDGETS = list(content)
        file.close()


    def access_budget(self):

        self.fill_select_field(self.ACCESS_HOME, self.ACCESS_BUDGET)

        self.click_button(self.CREATE_BUDGET)