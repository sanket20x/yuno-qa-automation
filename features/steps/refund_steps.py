from behave import given, when
from utils.api_client import send_post

@given("I have a completed payment id")
def step_payment_id(context):
    context.payment_id = "pay_test_id"

@when("I send refund request")
def step_refund(context):
    context.response = send_post(
        f"/payments/{context.payment_id}/refunds", {}
    )
