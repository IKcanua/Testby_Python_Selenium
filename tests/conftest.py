import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from abstract.selenium_listener import MyListener


@pytest.fixture
def get_chrome_options():
    option = chrome_options()
    option.add_argument('chrome')  # Use headless if you do not need a browser UI
    option.add_argument('--start-maximized')
    option.add_argument('--window-size=1650,900')
    return option


@pytest.fixture
def get_webdriver(get_chrome_options):
    option = get_chrome_options
    driver = webdriver.Chrome(options=option)

    return driver

#
@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, MyListener())
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    time.sleep(5)
    driver.find_element(By.ID, 'closeButton').click()
    yield driver
    driver.quit()



