from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from pages.realworld_base_page import RealworldCounduitBasePage

class RealworldPost(RealworldCounduitBasePage):

    URL = 'https://react-redux.realworld.io/'

    TIMESTAMP = datetime.timestamp(datetime.now())

    POST = {'title': 'Probando ' + str(TIMESTAMP), 'about': 'Se habla de probando probando',
                 'body': 'Hablando de mis pruebas', 'tags': 'solo son pruebas'}
    COMMENT = 'Comentario Simple'

    BUTTON_WAIT_LOCATOR = (By.XPATH, "//a/i[@class = 'ion-compose']")
    URL_VISIBILITY = (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/h1')
    SELECTOR_CREATE_POST = (By.XPATH, "//a/i[@class = 'ion-compose']")
    SELECTOR_TITLE_POST = '//*[@id="main"]//fieldset/fieldset[1]/input'
    SELECTOR_ABOUT_ARTICLE_POST = '//*[@id="main"]//fieldset/fieldset[2]/input'
    SELECTOR_BODY_ARTICLE_POST = "//textarea[@class = 'form-control']"
    SELECTOR_TAGS_ARTICLE_POST = (By.XPATH, "//input[@placeholder='Enter tags']")
    BUTTON_INTRO_ARTICLE_POST = "//button[@type='button']"

    def __init__(self, driver):
        self.driver = driver

    def wait_button(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(self.BUTTON_WAIT_LOCATOR))

    def register_new_post(self):

        create_post = self.driver.find_element(*self.SELECTOR_CREATE_POST)
        create_post.click()

        title_article = self.driver.find_element_by_xpath(self.SELECTOR_TITLE_POST)
        title_article.click()
        title_article.send_keys(self.POST['title'])

        about_article = self.driver.find_element_by_xpath(self.SELECTOR_ABOUT_ARTICLE_POST)
        about_article.click()
        about_article.send_keys(self.POST['about'])

        body_article = self.driver.find_element_by_xpath(self.SELECTOR_BODY_ARTICLE_POST)
        body_article.click()
        body_article.send_keys(self.POST['body'])

        self.fill_field(self.SELECTOR_TAGS_ARTICLE_POST, self.POST['tags'])

        intro_article = self.driver.find_element_by_xpath(self.BUTTON_INTRO_ARTICLE_POST)
        intro_article.send_keys(Keys.ENTER)
        title = self.POST['title']
        body = self.POST['body']

        return title, body


    def get_url(self):

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.visibility_of_element_located(self.URL_VISIBILITY))

        return self.driver.current_url

