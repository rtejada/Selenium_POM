from selenium.webdriver.common.by import By
from pages.suitecrm_base_page import SuitecrmBasePage
from random import randint


class ConfigureEmail(SuitecrmBasePage):
    EMAIL_DATA = ''

    BUTTON_ALL = (By.LINK_TEXT, 'TODO')
    ACCESS_CAMPAIGN = (By.LINK_TEXT, 'Campañas')
    CONFIGURE_EMAIL = (By.LINK_TEXT, 'Configurar Email')
    BUTTON_NEXT = (By.ID, 'wiz_next_button')
    CHECKBOX_CREATE = (By.ID, 'create_mbox')
    NAME_EMAIL = (By.ID, 'name')
    SENDER_ADDRESS = (By.ID, 'from_addr')
    URL_SERVER = (By.ID, 'server_url')
    EMAIL_USER = (By.ID, 'email_user')
    PROTOCOL = (By.ID, 'protocol')
    EMAIL_PASS = (By.ID, 'email_password')
    EMAIL_PORT = (By.ID, 'port')
    MONITORED_FOLDER = (By.ID, 'mailbox')
    SAVE_ID = 'wiz_submit_button'
    SAVE = (By.ID, SAVE_ID)

    def __init__(self, driver):
        super().__init__(driver)

        f = open("../data/email_data.txt", "r")
        self.EMAIL_DATA = f.readlines()
        f.close()

        self.EMAIL_DATA[0] = self.EMAIL_DATA[0].replace('\n', '') + str(randint(1, 90000000))
        self.EMAIL_DATA[1] = str(randint(1, 90000000)) + self.EMAIL_DATA[1].replace('\n', '')
        self.EMAIL_DATA[2] = str(randint(1, 90000000)) + self.EMAIL_DATA[2].replace('\n', '')
        self.EMAIL_DATA[3] = str(randint(1, 90000000)) + self.EMAIL_DATA[3].replace('\n', '')
        self.EMAIL_DATA[4] = self.EMAIL_DATA[4].replace('\n', '')
        self.EMAIL_DATA[5] = self.EMAIL_DATA[5].replace('\n', '')
        self.EMAIL_DATA[6] = self.EMAIL_DATA[6].replace('\n', '')
        self.EMAIL_DATA[7] = self.EMAIL_DATA[7].replace('\n', '')
        
    def access_campaign_all(self):

        self.menu_select_option(self.BUTTON_ALL, self.ACCESS_CAMPAIGN)

    def configure_email(self):

        self.click_button(self.CONFIGURE_EMAIL)

        self.click_button(self.BUTTON_NEXT)

        self.click_button(self.CHECKBOX_CREATE)

        self.fill_text_field(self.NAME_EMAIL, self.EMAIL_DATA[0])

        self.fill_text_field(self.SENDER_ADDRESS, self.EMAIL_DATA[1])

        self.fill_text_field(self.URL_SERVER, self.EMAIL_DATA[2])

        self.fill_text_field(self.EMAIL_USER, self.EMAIL_DATA[3])

        self.fill_select_field(self.PROTOCOL, self.EMAIL_DATA[4])

        self.fill_text_field(self.EMAIL_PORT, self.EMAIL_DATA[6])

        self.fill_text_field(self.MONITORED_FOLDER, self.EMAIL_DATA[7])

        self.click_by_javascript(self.SAVE_ID)

        self.click_button(self.BUTTON_NEXT)

        self.send_enter_key(self.SAVE)

        return self.EMAIL_DATA[0], self.EMAIL_DATA[1], self.EMAIL_DATA[3]





