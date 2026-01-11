from behave import given, when
from utils.api_client import send_post

@given("I have an authorization id")
def step_auth_id(context):
    context.auth_id = "auth_test_id"

@when("I send cancel request")
def step_cancel(context):
    context.response = send_post(f"/payments/{context.auth_id}/cancel", {})
