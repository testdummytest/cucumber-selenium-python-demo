
import pytest, logging, os
from selenium import webdriver
import chromedriver_autoinstaller
import xml.etree.ElementTree as ET
# from mobile import Dashboard
# import send_email

       
@pytest.fixture(scope="session")
def driver(request):
    try:
        chromedriver_autoinstaller.install()
        c = webdriver.ChromeOptions()   
        c.add_argument("--headless=new")
        c.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=c)
        request.node.driver = driver
        yield driver
    except Exception as e:
        logging.error(e)
    finally:
        driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    logging.info("In pytest_runtest_makereport")
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = getattr(item.session, "driver", None)
        logging.info(driver)
        if driver:
            screenshot_name = f"{item.name}.png".replace('[', "_").replace(']', "_")
            sanitized_name = "".join(c for c in screenshot_name if c.isalnum() or c in (" ", "-", "_", "."))
            screenshot_path = os.path.join("screenshots", sanitized_name)
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(screenshot_path)

def fetch():
    path = os.getcwd() + "/report/test.xml"
    tree = ET.parse(path)
    root = tree.getroot()
    test_results = []
    for testcase in root.findall('.//testcase'):
        test_classname = testcase.get('classname')
        test_name = testcase.get('name')
        time_taken = testcase.get('time')
        error_message = None
        failure = testcase.find('failure')
        if failure is not None:
            error_message = failure.get('message')
        if error_message:
            test_results.append([test_classname,test_name, "Fail" , time_taken, error_message])
        else:
            test_results.append([test_classname,test_name, "Pass", time_taken])
    # return test_results
    print(test_results)
    return test_results

# def pytest_unconfigure(config):
#     # dashboard_list = fetch()
#     # dashboard_main(dashboard_list)
#     send_to = ["yogesh@primeqasolutions.com"]
#     cc_list = ["yogesh@primeqasolutions.com"]
#     send_email.send_mail("automationreport477@gmail.com", send_to, cc_list, "Automation execution report: ","\n", "smtp.gmail.com", port=587)
