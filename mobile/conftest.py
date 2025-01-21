
import pytest, logging, os
from pytest_bdd import given, scenario, scenarios, when, then, parsers
from time import sleep
import random, json
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


@pytest.fixture()
def driver(request):
    try:
        c = Options()
        # c.add_argument("--headless=new")
        c.add_argument("--window-size=1920,1080")
        # c.add_argument("--no-sandbox")
        # # c.add_argument("enable-automation")
        # c.add_argument("--disable-blink-features=AutomationControlled")
        # c.add_argument("--disable-dev-shm-usage")
        # prefs={"download.default_directory":os.getcwd()+"/downloads"}
        # c.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(options=c)
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=c)
        # driver = webdriver.Remote(command_executor='http://selenium__standalone-chrome:4444/wd/hub',options=c)
        # driver = webdriver.Chrome()
        yield driver
    except Exception as e:
        raise e
    # finally:
    #     driver.quit()


