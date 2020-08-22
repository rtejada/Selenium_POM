from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


def get_driver():

    load_dotenv(os.getcwd() + "/tests/.env")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(",")
    options = Options()
    for i in args:
        options.add_argument(i)

    return webdriver.Chrome(options=options)
