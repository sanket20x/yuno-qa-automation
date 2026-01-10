from behave import then

@then("response status code should be {status_code:d}")
def step_verify_status_code(context, status_code):
    assert context.response is not None, "Response is None"
    assert context.response.status_code == status_code, (
        f"Expected {status_code}, got {context.response.status_code}"
    )
