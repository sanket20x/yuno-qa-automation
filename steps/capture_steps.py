from behave import given, when
from utils.api_client import send_post

@given("I have an authorized payment id")
def step_capture_id(context):
    context.auth_id = "auth_test_id"

@when("I send capture request")
def step_capture(context):
    context.response = send_post(f"/payments/{context.auth_id}/capture", {})
