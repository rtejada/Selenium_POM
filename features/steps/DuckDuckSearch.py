from behave import *
from selenium import webdriver

from lib.pages.results_page import DuckDuckGoResultsPage
from lib.pages.search_page import DuckDuckGoSearchPage

use_step_matcher("re")

@given("Visitamos la web de duckduckgo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver = webdriver.Chrome()

    search_page = DuckDuckGoSearchPage(context.driver)
    search_page.load()

    context.search_page = search_page


@when("se introduce la búsqueda panda")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.PHRASE = 'panda'
    context.search_page.search(context.PHRASE)


@then("hay resultados para esa búsqueda")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verify that results appear
    result_page = DuckDuckGoResultsPage(context.driver)

    assert (result_page.link_div_count() > 0)
    assert (result_page.phrase_result_count() > 0)
    assert (result_page.search_input_value() == context.PHRASE)

