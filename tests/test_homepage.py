import pytest
import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.driver.delete_all_cookies()
        # cookies = homepage_nav.driver.get_cookies()
        # cookies_names = [cookie['name'] for cookie in cookies]
        # print(cookies)
        # print('---------------------------------')
        # print(cookies_names)


        # actual_nav_links = homepage_nav.get_nav_links_text()
        # expected_nav_links = homepage_nav.NAV_LINK_TEXT
        # assert expected_nav_links == actual_nav_links, 'Validating Main Nav Link Texts'
        # elements = homepage_nav.get_nav_links()
        for indx in range(8):
            homepage_nav.get_nav_links()[indx].click()
            homepage_nav.driver.delete_all_cookies()

            # for cookie_name in cookies_names:
            #     homepage_nav.driver.delete_cookie('AMCVS_8D0867C25245AE650A490D4C%40AdobeOrg')
            #
            #     # homepage_nav.is_visible('tag_name', 'h1', cookie_name)
            #     time.sleep(0.5)
            #     homepage_nav.driver.refresh()
            # homepage_nav.driver.delete_all_cookies()


        # print(homepage_nav.get_nav_links_text())

    # def test_homepage(self):

    # pass
    # dr = webdriver.Chrome()
    # dr.implicitly_wait(10)
    # el1 = dr.find_element(By.CSS_SELECTOR, '#id_123')
    #
    # wt = WebDriverWait(dr, 15, 0.3)
    # el2 = wt.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_123')))
