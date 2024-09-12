import time

from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class SearchPage(BasePage):
    input_field = (By.XPATH, "//input[@type='search']")
    result = (By.XPATH, "//li/a[contains(@href,'/directory')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def click_on_input_field(self):
        try:
            self.web_utils.find_element(*self.input_field).click()
        except Exception:
            raise Exception('Can not click on the input field')

    def search(self, words):
        try:
            self.web_utils.find_element(*self.input_field).send_keys(words)
        except Exception:
            raise Exception('Can not fill the search form')

    def click_first_result(self):
        try:
            self.web_utils.find_element(*self.result).click()
        except Exception:
            raise Exception('Can not click on the searched element')
