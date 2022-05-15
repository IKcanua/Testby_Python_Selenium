from selenium.webdriver.support.events import AbstractEventListener

from base.seleniumbase import SeleniumBase


class MyListener(AbstractEventListener):
    # def __init__(self, driver):
    #     self.selenium_base = SeleniumBase(driver)

    def before_click(self, element, driver):
        SeleniumBase(driver).delete_all_cookies()

    def after_click(self, element, driver):
        SeleniumBase(driver).delete_all_cookies()
