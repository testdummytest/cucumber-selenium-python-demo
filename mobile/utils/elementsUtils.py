import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10
POLL_FREQUENCY = 0.5

class ElementsUtils:

    @staticmethod            
    def send_keys(driver, locator, data):
        element = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(data)
        
    @staticmethod
    def get_text(driver, locator):
        element = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        if element:
            text_value = element.text.strip()
            logging.info(f"Element text: {text_value}")
            return text_value
        return None
    
    @staticmethod
    def click_element(driver, locator):
        element = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        element = ElementsUtils.getelementifclickable(driver, locator)
        element.click()
        
    @staticmethod
    def getelementifclickable(driver, locator):
        return WebDriverWait(driver, TIMEOUT, POLL_FREQUENCY).until(
            ec.element_to_be_clickable(locator), f"Element {locator} is not clickable"
        )
