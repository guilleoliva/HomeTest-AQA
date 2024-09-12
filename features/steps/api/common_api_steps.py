import requests
from yaml import safe_load
from behave import *

requests.packages.urllib3.disable_warnings()


@step("Tom is told the get facts list request was successful")
@step("Tom is told the get fact by its ID request was successful")
def get_entity_response(context):
    assert (
            context.response.status_code == 200
    ), f"Expected status code 200, current {context.response.status_code}"
    assert (
            context.response.reason == "OK"
    ), f"Expected reason OK, current {context.response.reason}"


def parse_text(context):
    try:
        if context.text:
            return safe_load(context.text)
        return {}
    except Exception:
        raise ValueError(f"{context.text} is not a valid YAML")
