
import pytest, logging, os
from pytest_bdd import given, scenario, scenarios, when, then, parsers
from time import sleep
import random, json
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from mobile.Report_Mail import *


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


# @pytest.fixture(scope="session", autouse=True)
# def jama_init(request):
#     print(f"{jama_init.__name__}: Checking if JAMA is being used or not...")
#     CLIENT_ID = os.getenv("JAMA_CLIENT_ID")
#     CLIENT_SECRET = os.getenv("JAMA_CLIENT_SECRET")
#     TEST_PLAN_ID = 17125021
 
#     if TEST_PLAN_ID and CLIENT_ID is not None and os.getenv("JAMA_ENABLED") == "true":
#         cycle_id = os.getenv("TEST_CYCLE_ID")
#         # cycle_id = "16463243" #it can be gathered inspecting the page for an specific commit
#         print(f"JAMA_CLIENT: {cycle_id}")
#         jamatest.init(CLIENT_ID, CLIENT_SECRET, TEST_PLAN_ID, cycle_id)
#         request.addfinalizer(publish_results)
 
# def publish_results():
#     if os.getenv("JAMA_ENABLED") == "true":
#         jamatest.publish()
 
# def pytest_addoption(parser):
#     parser.addoption("--env", action="store")
 
 
# def pytest_configure(config):
#     os.environ["env"] = config.getoption("env")
 
# from main_test.Delete_Automation_Data import *
 
# def pytest_unconfigure(config):
#     # Deletion_Automation_Data()
#     # Error_Table_Generation()
#     TestReport_Generation()
#     # Summary_Table_Formation()
#     Send_Mail()
#     # logging.info("finally")