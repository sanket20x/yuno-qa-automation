from behave import given, when
from utils.payload_factory import customer_payload
from utils.api_client import send_post

@given("I prepare customer payload")
def step_customer(context):
    context.payload = customer_payload()

@given("I prepare invalid customer payload")
def step_invalid_customer(context):
    payload = customer_payload()
    payload.pop("merchant_customer_id")
    context.payload = payload

@when("I send create customer request")
def step_send_customer(context):
    context.response = send_post("/customers", context.payload)
