from time import sleep
import logging
from selenium.webdriver.common.by import By
from mobile.utils.elementsUtils import ElementsUtils
from mobile.utils.assertionUtils import AssertionUtils
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class RegisterPageLocators:
    
    FIRSTNAME = (By.XPATH, '//input[@formcontrolname="firstName"]')
    ERROR_PATH = (By.XPATH, '(//span[@class="ng-star-inserted"])[1]')
    LASTNAME = (By.XPATH, '//input[@formcontrolname="lastName"]')
    LNAME_ERROR = (By.XPATH, '(//span[@class="ng-star-inserted"])[2]')
    REGISTER_BTN = (By.XPATH, '//button[span[text()="Register"]]')
    EMAIL = (By.XPATH, '//input[@formcontrolname="email"]')
    COUNTRY_ERROR = (By.XPATH, '(//span[@class="ng-star-inserted"])[6]')
    PHONE = (By.XPATH, '//input[@id="withoutgrouping"]')
    
class RegisterLocators:

    @staticmethod
    def send_firstname(driver, firstname):
        firstname_locator = RegisterPageLocators.FIRSTNAME
        ElementsUtils.send_keys(driver, firstname_locator, firstname)
        
    @staticmethod
    def validate_firstname(driver, errormsg):
        fname_error = RegisterPageLocators.ERROR_PATH
        assert ElementsUtils.get_text(driver,fname_error) == errormsg
        
    @staticmethod
    def send_lastname(driver, lastname):
        lastname_locator = RegisterPageLocators.LASTNAME
        ElementsUtils.send_keys(driver, lastname_locator, lastname)
        
    @staticmethod
    def validate_lastname(driver, errormsg):
        lname_error = RegisterPageLocators.LNAME_ERROR
        assert ElementsUtils.get_text(driver,lname_error) == errormsg
        
    @staticmethod
    def send_email(driver, email):
        email_locator = RegisterPageLocators.EMAIL
        ElementsUtils.send_keys(driver, email_locator, email)
        
    @staticmethod
    def validate_email(driver, errormsg):
        email_error = RegisterPageLocators.ERROR_PATH
        assert ElementsUtils.get_text(driver,email_error) == errormsg
        
        
    def register_btn_default_enabled(driver):
        
        register_btn_locator = RegisterPageLocators.REGISTER_BTN
        try:
            register_btn_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(register_btn_locator)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", register_btn_element)
        except TimeoutException:
            print("The 'Register' button was not found within 10 seconds.")

        try:
            # register_button = driver.find_element(By.XPATH, RegisterPageLocators.REGISTER_BTN)
            assert register_btn_element.is_enabled(), "AssertionError: The 'Register' button is not enabled by default."
            logging.info("The Register button is enabled by default.")
        except AssertionError as e:
            logging.info(str(e))
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            

    @staticmethod
    def user_validate_country_field(driver, errormsg):
        
        register_btn_locator = RegisterPageLocators.REGISTER_BTN
        try:
            register_btn_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(register_btn_locator)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", register_btn_element)
        except TimeoutException:
            print("The 'Register' button was not found within 10 seconds.")
            
        ElementsUtils.click_element(driver, register_btn_locator)
        
        country_error = RegisterPageLocators.COUNTRY_ERROR
        assert ElementsUtils.get_text(driver,country_error) == errormsg

        
    @staticmethod
    def send_phone(driver, phonenumber):
        phone_locator = RegisterPageLocators.PHONE
        ElementsUtils.send_keys(driver, phone_locator, phonenumber)
        
    @staticmethod
    def validate_phone(driver, errormsg):
        phone_error = RegisterPageLocators.ERROR_PATH
        assert ElementsUtils.get_text(driver,phone_error) == errormsg
        