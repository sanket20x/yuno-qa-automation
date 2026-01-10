from behave import given, when
from utils.payload_factory import authorization_payment
from utils.api_client import send_post

@given("I prepare authorization payload")
def step_prepare_auth(context):
    context.payload = authorization_payment()

@when("I send authorization request")
def step_send_auth(context):
    context.response = send_post("/payments", context.payload)
