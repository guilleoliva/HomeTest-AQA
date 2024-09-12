import time

from behave import step

from features.pages.directory_page import DirectoryPage
from features.pages.landing_page import LandingPage
from features.pages.search_page import SearchPage
from features.pages.streamer_page import StreamerPage


@step("Tom goes to {app_name} Web APP login page")
def open_app(context, app_name):
    context.execute_steps(
        """
        Given a browser
    """
    )
    context.browser.driver.maximize_window()
    app_url = context.env_config["app_url"]
    landing_page = LandingPage(context.browser.driver, app_url)
    landing_page.open_app()
    context.current_page = landing_page
    assert app_url in landing_page.get_current_url()


@step("Tom should see the Twitch logo present")
def logo_presence(context):
    assert context.current_page.is_logo_present()


@step("Tom clicks on search")
def click_on_search(context):
    context.current_page.click_on_search()


@step('Tom searches for "{}"')
def search(context, words):
    context.current_page = SearchPage(context.browser.driver)
    context.current_page.click_on_input_field()
    context.current_page.search(words)


@step("Tom selects the first result")
def first_result(context):
    time.sleep(2)
    context.current_page.click_first_result()


@step("Tom scrolls down {} times")
def scrolls_down(context, times):
    context.current_page = DirectoryPage(context.browser.driver)
    context.current_page.scroll_down(times)


@step("Tom selects a streamer in view")
def selects_streamer(context):
    context.current_page.select_streamer()


@step("Tom takes an snapshot")
def take_snapshot(context):
    streamer_page = StreamerPage(context.browser.driver)
    streamer_page.is_data_target_message_present()
    assert streamer_page.is_follow_button_present()
    streamer_page.take_snapshot()
