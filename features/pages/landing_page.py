import time

from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class LandingPage(BasePage):
    twitch_logo = (By.XPATH, "//a[@interactioncontent='logo']")
    search = (By.XPATH, "//a[@href='/search']")

    def __init__(self, driver, app_url):
        super().__init__(driver)
        self.login_url = app_url
        self.page_loading_time = time.time() - self.start_time

    def open_app(self):
        self.web_utils.get(self.login_url)

    def is_logo_present(self):
        try:
            return True if self.web_utils.find_element(*self.twitch_logo).is_displayed() else False
        except Exception:
            raise Exception('Can not find the Twitch Logo')

    def click_on_search(self):
        try:
            search = self.web_utils.find_element(*self.search)
            search.click()
        except Exception as e:
            raise Exception(f'Can not click on the search button {e}')






