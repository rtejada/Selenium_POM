from behave import *
from dotenv import load_dotenv
from selenium import webdriver
import os
from lib.pages.realworld_home import RealworldHome
from lib.pages.realworld_post import RealworldPost
from lib.pages.realworld_confirm_post import PostPage

use_step_matcher("re")


@given("El usuario se ha registrado en el sistema")
def realworld_page(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.counduit")

    context.driver = webdriver.Chrome()
    home = RealworldHome(context.driver)
    home.load()
    home.init_session()


@when("Registra un nuevo producto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    post = RealworldPost(context.driver)
    post.wait_button()
    context.title_article, context.body_article = post.register_new_post()
    context.post_url = post.get_url()


@then("Se comparan los resultados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    confirm_post = PostPage(context.driver)
    confirm_post.open_window_of_post(context.post_url)
    confirm_post.wait_button()
    title, body = confirm_post.data_test()

    assert(context.title_article == title)
    assert(context.body_article == body)

