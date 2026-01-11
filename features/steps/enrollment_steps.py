from behave import given, when
from utils.api_client import send_request

@given("I have a customer")
def step_customer(context):
    context.customer_id = "customer_test_id"

@when("I send enrollment request")
def step_enroll(context):
    context.response = send_request(
        "POST",
        f"/customers/{context.customer_id}/payment-methods"
    )
