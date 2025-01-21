import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.appiumby import AppiumBy
from mobile.utils.elementsUtils import ElementsUtils

TIMEOUT = 10


# The AssertionUtils class provides methods for asserting element visibility, checking for specific
# text on a page, and verifying the presence of an element on a page.
class AssertionUtils:

    @staticmethod
    def assert_element_displayed(driver, locator):
        try:
            element = WebDriverWait(driver, TIMEOUT).until(ec.visibility_of_element_located(locator))
            assert element.is_displayed(), f"Element is not displayed."
        except AssertionError:
            raise AssertionError(f"Element {element} is not displayed.")
        except TimeoutException:
            raise TimeoutException(f"Element {locator} is not found within the specified timeout.")