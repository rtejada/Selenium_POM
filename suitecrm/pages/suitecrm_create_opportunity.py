from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
from random import randint


class CreateNewOpportunity(SuitecrmBasePage):

    OPPORTUNITIES = {'name_opportunity': 'Traime un amigo', 'close_date': '31/07/2020', 'amount_opprtunity': '1500', 'type': 'Tournefeuille', 'tel': '034-829875', 'mobile': '689457815', 'workingStation': 'Administrativo',
                'departament': 'Toulose_Depart', 'email': '@toulouse.fr', 'address': '138 Saint-Geniès-Bellevue', 'city': 'Saint-Bellevue', 'CP': '31200',
                'country': 'Francia', 'description': 'Esperas explícitas disponibles para clientes de Selenium'}

    BUTTON_CREATE = (By.LINK_TEXT, 'Crear')
    CREATE_OPPORTUNITY = (By.LINK_TEXT, 'Crear Oportunidades')

    def __init__(self, driver):
        super().__init__(driver)
        self.OPPORTUNITIES['name_opportunity'] = self.OPPORTUNITIES['name_opportunity'] + ' ' + str(randint(1, 90000000))
        self.OPPORTUNITIES['email'] = str(randint(1, 90000000)) + (self.OPPORTUNITIES['email'])

    def page_contact(self):

        self.menu_select_option(self.BUTTON_CREATE, self.CREATE_OPPORTUNITY)

    def create_new_contact(self):
        pass