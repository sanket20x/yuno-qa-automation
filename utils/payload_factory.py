from config.config import ACCOUNT_ID

def base_payment():
    return {
        "account_id": ACCOUNT_ID,
        "amount": 1000,
        "currency": "USD",
        "workflow": "DIRECT",
        "capture": True,
        "payment_method": {
            "type": "CARD",
            "token": "test_token",
            "detail": {
                "card": {
                    "number": "4507990000000002",
                    "expiration_month": "11",
                    "expiration_year": "28",
                    "security_code": "123",
                    "holder_name": "Sanket Bagade"
                }
            }
        }
    }


def payment_with_customer_and_additional():
    payload = base_payment()
    payload["customer_payer"] = {
        "id": "cust_test_123"
    }
    payload["additional_data"] = {
        "note": "extra data"
    }
    return payload

def customer_payload():
    return {
        "account_id": ACCOUNT_ID,
        "merchant_customer_id": "cust_test_123",
        "email": "test@example.com",
        "name": "Test Customer"
    }

def authorization_payment():
    payload = base_payment()
    payload["capture"] = False
    return payload

def insufficient_funds_payment():
    payload = base_payment()
    payload["payment_method"]["detail"]["card"]["number"] = "4507990000000010"
    return payload

def verify_payment():
    payload = base_payment()
    payload["verify"] = True
    return payload
