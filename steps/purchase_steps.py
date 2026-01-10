from behave import given, when
from utils.payload_factory import (
    base_payment,
    insufficient_funds_payment
)
from utils.api_client import send_post

@given("I prepare minimal purchase payload")
def step_min(context):
    context.payload = base_payment()

@given("I prepare insufficient funds payload")
def step_insufficient(context):
    context.payload = insufficient_funds_payment()

@when("I send purchase request")
def step_purchase(context):
    context.response = send_post("/payments", context.payload)
