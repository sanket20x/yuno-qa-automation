# Payment API Automation Framework (BDD – Python)

## Project Overview
This project is a **BDD-based API automation framework** built using **Python and Behave** to validate payment-related APIs.  
The goal of this framework is to verify API request construction, payload handling, headers, and overall API flow using **Gherkin scenarios**.

This framework focuses on **structural and integration-level validation**, not real transaction execution.


## Tech Stack
- Language: Python
- BDD Framework: Behave
- API Testing: Requests library
- Test Design: Gherkin (BDD)
- Configuration: Environment-based config handling

## Project Folder Structure
project-root/
│
├── README.md
├── requirements.txt
│
├── config/
│ └── config.py
│
├── features/
│ ├── authorization.feature
│ ├── cancel.feature
│ ├── capture.feature
│ ├── customer.feature
│ ├── enrollment.feature
│ ├── purchase.feature
│ ├── refund.feature
│ ├── verify.feature
│ └── environment.py
│
├── payloads/
│ └── payment_payloads.py
│
├── steps/
│ ├── authorization_steps.py
│ ├── cancel_steps.py
│ ├── capture_steps.py
│ ├── customer_steps.py
│ ├── enrollment_steps.py
│ ├── purchase_steps.py
│ ├── refund_steps.py
│ └── verify_steps.py
│
└── utils/
└── api_client.py



## Configuration
All environment-level configurations such as:
- Base URL
- Account ID
- API headers
- API keys

are maintained inside:
config/config.py


## Payload Management
All reusable API payloads are centralized in:
payloads/payment_payloads.py


This includes:
- Authorization payloads
- Purchase payloads
- Verification payloads
- Insufficient funds payloads
- Customer-linked payment payloads

This structure avoids duplication and improves maintainability.

## BDD Feature Coverage
Each payment flow is covered using separate Gherkin feature files:
- Authorization
- Purchase
- Capture
- Cancel
- Refund
- Verify
- Customer creation
- Payment method enrollment

Scenarios are written in business-readable language for clarity and traceability.


## Step Definitions
Step definition files map Gherkin steps to Python code and perform:
- Request preparation
- API invocation
- Response validation
- Status code verification
- Logging for debugging



## How to Run the Tests

### Install Dependencies
```bash
pip install -r requirements.txt
Execute All Tests
bash
Copy code
behave
Execute a Specific Feature
bash
Copy code
behave features/purchase.feature
Test Execution Result
All scenarios execute successfully and reach the API layer.

Failures with HTTP 404 are expected because:

No real merchant account was provided

API keys and account_id are placeholders

Endpoints are validated structurally, not functionally

This confirms the correctness of:

Gherkin scenarios

Step definitions

Request construction

Header and payload handling

Key Highlights
BDD-based API automation framework

Modular and reusable payload design

Clear separation of concerns

Supports positive and negative scenarios

Easy to extend for real environments

Author
Sanket Bagade
Hyderabad, India