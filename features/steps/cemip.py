from behave import *
from selenium import webdriver
from lib.pages.cemip_home import CualEsMiIpHome
from lib.pages.cemip_geo import CualEsMiIpGeo
from lib.pages.cemip_maxmind import CualEsMiIpMaxMind
from dotenv import load_dotenv
import os

use_step_matcher("re")


@given("Acceder a CualEsMiIp")
def home_cemip(context):
    """
    :type context: behave.runner.Context
    """

    load_dotenv(os.getcwd() + "/features/lib/data/.env.cualesmiip")

    context.driver = webdriver.Chrome()

    home_page = CualEsMiIpHome(context.driver)
    home_page.load()
    context.home_page = home_page


@step("Cargar Geolocalización")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home_page.press_button()
    context.home_page.wait_element_visible()


@when("Obtener los datos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    geo = CualEsMiIpGeo(context.driver)

    context.cemip_data = geo.get_data()


@then("Comparar resultados con MaxMind")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    maxm = CualEsMiIpMaxMind(context.driver)

    maxm.load()
    maxm.wait_element_visible()

    maxmip_data = maxm.get_data()

    assert(context.cemip_data.ip == maxmip_data.ip)
    assert(context.cemip_data.country == maxmip_data.country)
    assert(context.cemip_data.city == maxmip_data.city)
    assert(context.cemip_data.lat == maxmip_data.lat)
    assert(context.cemip_data.lon == maxmip_data.lon)
    assert(context.cemip_data.isp == maxmip_data.isp)

