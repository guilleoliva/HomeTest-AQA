import os
import time

from .web_utils import WebUtils


class BasePage:
    page_loading_time = 0
    xpath_lower_text = ("translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')")
    xpath_lower_string = "translate(string(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"

    def __init__(self, driver):
        self.start_time = time.time()
        self.driver = driver
        self.web_utils = WebUtils(driver)

    def get_page_loading_time(self):
        return self.page_loading_time

    def get_current_url(self):
        return self.driver.current_url

    def go_to_previous_page(self):
        return self.driver.back()

    def take_snapshot(self):
        self.web_utils.driver.save_screenshot(os.path.join(os.environ.get("OUTPUT"), 'screenshot.png'))
