import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class DirectoryPage(BasePage):
    header = (By.XPATH, "//h1[text()='StarCraft II']")
    popup = (By.XPATH, "//h2[@id='modal-root-header']")
    close_popup = (By.XPATH, "//button[@data-a-target='modalClose']")
    streamers = (By.XPATH, "//a[contains(@class,'tw-link') and @href]/div/div/img")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def scroll_down(self, times):
        try:
            self.web_utils.find_element(*self.header, log_errors=False)
            for i in range(int(times)):
                self.web_utils.driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(2)
        except Exception:
            raise Exception('Can not scroll down')

    def select_streamer(self):
        actions = ActionChains(self.web_utils.driver)
        time.sleep(2)
        in_view_script = """
        var elem = arguments[0],
            box = elem.getBoundingClientRect(),
            cx = box.left + box.width / 2,
            cy = box.top + box.height / 2,
            e = document.elementFromPoint(cx, cy);
        for (; e; e = e.parentElement) {
            if (e === elem)
                return true;
        }
        return false;
        """
        try:
            div_elements = self.web_utils.find_elements(*self.streamers)
            for div in div_elements:
                if self.web_utils.driver.execute_script(in_view_script, div):
                    actions.move_to_element(div).click().perform()
                    try:
                        popup = self.web_utils.find_element(*self.popup, retries=3, log_errors=False)
                        if popup.is_displayed():
                            self.web_utils.find_element(*self.close_popup).click()
                        time.sleep(2)
                        actions.move_to_element(div).click().perform()
                    except Exception:
                        pass
                    break
        except:
            raise Exception('Can not select a streamer')