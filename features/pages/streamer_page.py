import time

from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class StreamerPage(BasePage):
    follow_button = (By.XPATH, "//button[@data-a-target='follow-button']")
    data_target = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def is_data_target_message_present(self):
        try:
            self.web_utils.find_element(*self.data_target, log_errors=False, retries=5).click()
        except Exception:
            pass

    def is_follow_button_present(self):
        try:
            follow_button = self.web_utils.find_element(*self.follow_button)
            return True if follow_button.is_displayed() else False
        except Exception:
            raise Exception('Can not find the follow button')

