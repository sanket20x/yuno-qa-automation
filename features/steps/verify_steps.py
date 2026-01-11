from behave import given, when
from utils.payload_factory import verify_payment
from utils.api_client import send_post

@given("I prepare verify payment payload")
def step_verify_payload(context):
    context.payload = verify_payment()

@when("I send verify request")
def step_verify(context):
    context.response = send_post("/payments", context.payload)
