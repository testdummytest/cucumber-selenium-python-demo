from pytest_bdd import when, then, given, parsers
from pytest_bdd.parsers import parse
from pytest_bdd.parsers import cfparse as Parser
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import logging
from mobile.locators.registerPageLocators import RegisterLocators
    
@given(Parser('User open browser and navigates to the {link} page'))
def open_browser(driver, link):
    driver.get(link)
    driver.maximize_window()
    
@when(Parser('User enters {firstname}'))
def enters_firstname(driver, firstname):
    RegisterLocators.send_firstname(driver, firstname)
    
@when(Parser('User validate the firstname error msg {errormsg}'))
def validate_firstname(driver, errormsg):
    RegisterLocators.validate_firstname(driver, errormsg)
    
@when(Parser('User is enter {lastname}'))
def enters_lastname(driver, lastname):
    RegisterLocators.send_lastname(driver, lastname)
    
@when(Parser('User is validate the lastname error msg {errormsg}'))
def validate_lastname(driver, errormsg):
    RegisterLocators.validate_lastname(driver, errormsg)
    
@when(Parser('User now enter the {email}'))
def enters_email(driver, email):
    RegisterLocators.send_email(driver, email)
    
@when(Parser('User want to validate the email error msg {errormsg}'))
def validate_email(driver, errormsg):
    RegisterLocators.validate_email(driver, errormsg)
    
@when(Parser('User see register button is default enabled'))
def register_btn_default_enabled(driver):
    RegisterLocators.register_btn_default_enabled(driver)
    
@when(Parser('User validate country field {errormsg}'))
def user_validate_country_field(driver, errormsg):
    RegisterLocators.user_validate_country_field(driver, errormsg)

@when(Parser('User want to enters a {phonenumber}'))
def enters_phone(driver, phonenumber):
    RegisterLocators.send_phone(driver, phonenumber)
    
@when(Parser('User is validates phonenumber error msg {errormsg}'))
def validate_phone(driver, errormsg):
    RegisterLocators.validate_phone(driver, errormsg)