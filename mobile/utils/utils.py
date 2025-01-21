# # This file contains reusable functions and utilities that are used across multiple test cases or modules.
# # IN THIS FILE ONLY CONFIGURATION METHOD MUST BE INCLUDED
# # These common methods serve to abstract away repetitive tasks, improve code readability, and promote code reusability.
# import json, os, logging
# import random
# from time import sleep
# import threading
# from appium.options.android import UiAutomator2Options
# from appium.options.ios import XCUITestOptions
# from mobile.conftest import driver
# from mobile.locators.loginPageLocators import LoginLocators, LoginPageLocators


# POLL_FREQUENCY = 0.1
# TIMEOUT = 20  # 5 seconds
# devices_in_use = {}
# device_lock = threading.Lock()
# class Utils:

#     @staticmethod
#     def get_config():
#         with open('config.json') as f:
#             config = json.load(f)
#         return config