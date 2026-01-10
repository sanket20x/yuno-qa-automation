import requests
import uuid
from config.config import BASE_URL, PUBLIC_API_KEY, PRIVATE_SECRET_KEY


def _headers():
    return {
        "public-api-key": PUBLIC_API_KEY,
        "private-secret-key": PRIVATE_SECRET_KEY,
        "x-idempotency-key": str(uuid.uuid4()),
        "Content-Type": "application/json"
    }


def send_post(endpoint, payload):
    url = BASE_URL + endpoint
    return requests.post(url, json=payload, headers=_headers())


def send_request(method, endpoint, payload=None):
    url = BASE_URL + endpoint
    return requests.request(
        method=method,
        url=url,
        json=payload,
        headers=_headers()
    )
