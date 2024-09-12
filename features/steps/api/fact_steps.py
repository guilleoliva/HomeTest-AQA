import json
import uuid

from behave import *

from features.steps.api.common_api_steps import parse_text
from utils.api_utils import (
    requests_get
)


@step('The fact exists with the following data')
def fact_data(context):
    context.fact_data = parse_text(context)


@step('Tom wants to get a fact for his ID "{}"')
def get_fact_by_id(context, factId):
    context.fact_id = factId
    url = "facts/" + context.fact_id
    context.response = requests_get(context, url)


@step("Tom verifies that all the fact information is correct")
def verify_fact_information(context):
    fact_received = context.response.json()
    assert fact_received["_id"] == context.fact_data["fact"]["_id"], (
            "The fact ID doesn't match, expected "
            + context.fact_data["fact"]["_id"]
            + " current "
            + fact_received["_id"]
    )
    assert fact_received["type"] == context.fact_data["fact"]["type"], (
            "fact type doesn't match, expected "
            + context.fact_data["fact"]["type"]
            + " current "
            + fact_received["type"]
    )
    assert fact_received["text"] == context.fact_data["fact"]["text"], (
            "fact text doesn't match, expected "
            + context.fact_data["fact"]["text"]
            + " current "
            + fact_received["text"]
    )
    assert fact_received["status"]["verified"] == context.fact_data["fact"]["status"]["verified"], (
            "fact status doesn't match, expected "
            + context.fact_data["fact"]["status"]["verified"]
            + " current "
            + fact_received["status"]["verified"]
    )
    assert fact_received["status"]["sentCount"] == context.fact_data["fact"]["status"]["sentCount"], (
            "fact count doesn't match, expected "
            + context.fact_data["fact"]["status"]["sentCount"]
            + " current "
            + fact_received["status"]["sentCount"]
    )


@step('Tom wants to get a "{}" facts filtered by "{}"')
def get_fact_list(context, fact_count, fact_type):
    context.fact_count = fact_count
    context.fact_type = fact_type
    url = "facts/random?animal_type=" + context.fact_type + "&amount=" + context.fact_count
    context.response = requests_get(context, url)


@step('Tom verifies that he received an empty array')
@step('Tom verifies that he received the correct amount of facts')
def verify_fact_amount(context):
    context.fact_received = context.response.json()
    fact_count = len(context.fact_received)
    if fact_count == 0:
        assert context.fact_received == [], f'an empty array was not received'
    else:
        assert str(fact_count) == context.fact_count, (
                "Amount of facts doesn't match, expected "
                + context.fact_count
                + " current "
                + str(fact_count)
        )


@step('Tom verifies that the facts received are of type cat')
def verify_patient_created(context):
    for index, count in enumerate(context.fact_received):
        assert context.fact_received[index]["type"] == context.fact_type
