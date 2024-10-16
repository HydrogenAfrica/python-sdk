# Hydrogen Python SDK

## Introduction

The Python library facilitates seamless payments via card transactions and account transfers, ensuring faster delivery of goods and services. 
Seamlessly integrate Hydrogen APIs with Flask, Django, and other Python applications. Our library simplifies direct integration, enabling rapid and efficient API requests.

Python library for [Hydrogen](https://hydrogenpay.com/)
View on [pypi.python.org](https://pypi.org/project/hydrogenpay-python/1.0.2/)

Key features:

- Collections: Card, Transfers, Payments, Bank Transfers.
- Recurring payments: Subscription-based payments.
- Confirmation: Payment Confirmation.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Initialization](#initialization)
4. [Usage](#usage)
5. [Testing](#testing)
5. [Support](#Support)
6. [Contribution](#Contribution)
7. [License](#License)
7. [ Hydrogenpay API References](#Hydrogenpay API References)


## Requirements
2. Supported Python versions: >=2.7, !=3.0.\*, !=3.1.\*, !=3.2.\*, !=3.3.\*, !=3.4.\*


## Installation
To install the library, run

```sh

pip install hydrogenpay_python


```

## Initialization

```py
from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions


# Initialize Hydrogenpay with API keys from environment variables
hydrogenpay = Hydrogenpay("YOUR SANDBOX_API_KEY", "YOUR SECRET API_KEY", 'test', setEnv=True)

# Initialize Hydrogenpay without API keys from environment variables
# hydrogenpay = Hydrogenpay(os.getenv("SANDBOX_API_KEY"), os.getenv("LIVE_API_KEY"), os.getenv("MODE"), setEnv=False)
hydrogenpay = Hydrogenpay("YOUR SANDBOX_API_KEY", "YOUR SECRETE API_KEY", 'test', setEnv=False)

# Call the PaymentService class to confirm the payment status
response = self.hydrogenpay.PaymentService.confirmpayment(txRef)

# Call the Transfer class to initiate a transfer and validate the response
response = self.hydrogenpay.Transfer.initiate(transfer_details)

# Call the PaymentService class to initiate a payment and validate the response
response = self.hydrogenpay.PaymentService.initiate(payment_details)

# Call the BankTransfer class to simulate a bank transfer
response = self.hydrogenpay.BankTransfer.simulatetransfer(transfer_details)


```

# Usage
This documentation covers all components of the hydrogen_python SDK.

## ```Payment```
This is used to facilitating the completion of payments through their preferred methods, including card or bank transfer..


*Usage*

```python

from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions
import logging #If Using Logging instead of print.


# Mock data for initiating a payment
        payment_details = {
            "amount": "50",
            "currency": "NGN",
            "email": "devtest@randomuser.com",
            "customerName": "Dev Test",
            "meta": "Test transaction",
            "callback": "https://webhook.site/43309fe4-a1f7-406d-afff-09e1cb12b9ec", #"https://example.com/callback"
            "isAPI": True
        }

        try:
            # Call the Transfer class to initiate a transfer and validate the response
            response = self.hydrogenpay.PaymentService.initiate(payment_details)
            # print(f"Payment initiation success: {response}")
            logger.info("Payment initiation successful:")
            logger.info(json.dumps(response, indent=4))


        except HydrogenpayExceptions.PaymentInitiateError as e:
            # Mark test as failed if payment initiation fails
            self.fail(f"Payment initiation failed: {e}")

```

*Arguments*

- `amount`: Amount to debit the customer.
- `currency`: Default to NGN if not passed, other currencies available are USD and GBP.
- `email`: Customer’s Email Address.
- `customerName`: Customer's name.
- `meta`: Customer's email address
- `callback`: Redirect URL after payment has been completed on the gateway.
- `isAPI`: Amount in kobo


*Returns*

Response Example:

```py
Payment initiation successful:
{
    "error": false,
    "validationRequired": true,
    "txRef": "36934683_766196b316",
    "authUrl": "https://payment.hydrogenpay.com?transactionId=94850000-d1b0-2648-175f-08dce946623e&Mode=19289182"
}

```


## ```Confirm Payment```

This allows businesses to verify the status of initiated payments using the transaction reference. This process utilizes the transaction reference to retrieve the specified payment's current status (e.g., success, failed, pending).

*Usage*

```python

from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions
import logging #If Using Logging instead of print.

 # Transaction reference obtained from a previous payment initiation
        txRef = "36934683_87087a9180"  # Replace with an actual reference

        try:
            # Call the SDK to confirm the payment status
            response = self.hydrogenpay.PaymentService.confirmpayment(txRef)

            logger.info("Payment confirmation successful:")
            logger.info(json.dumps(response, indent=4))


        except HydrogenpayExceptions.TransactionVerificationError as e:
            # Fail the test if transaction confirmation fails
            self.fail(f"Transaction confirmation failed: {e}")

```

*Arguments*

- `txRef`: Transaction Ref that is returned oncallback 


*Returns*

Response Example:

```py
Payment confirmation successful:
{
    "id": "94850000-d1b0-2648-4dda-08dce8bc64e0",
    "amount": 50.0,
    "chargedAmount": 50.0,
    "currency": "NGN",
    "customerEmail": "bwitlawalyusuf@gmail.com",
    "narration": null,
    "description": null,
    "status": "Paid",
    "transactionStatus": "Paid",
    "transactionRef": "36934683_87087a9180",
    "processorResponse": null,
    "createdAt": "2024-10-09T23:45:02.3685068",
    "paidAt": "2024-10-09T23:45:02.3685068",
    "ip": "145.224.74.164",
    "paymentType": "Card",
    "authorizationObject": null,
    "fees": 0.5,
    "vat": 0.04,
    "meta": "Test Py transaction",
    "recurringCardToken": "",
    "metadata": null,
    "error": false,
    "transactionComplete": true
}
```


## ```Transfer```

Generates dynamic virtual account details for completing payment transactions. Customers can request these details to facilitate payments through bank transfers.


*Usage*

```python

from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions
import logging #If Using Logging instead of print.

 # Mock data for initiating a bank transfer
        payment_details = {
            "amount": "50",
            "currency": "NGN",
            "email": "bwitlawalyusuf@gmail.com",
            "customerName": "Lawal Yusuf",
            "meta": "Test transaction",
            "callback": "https://webhook.site/43309fe4-a1f7-406d-afff-09e1cb12b9ec", #"https://example.com/callback"
            "isAPI": True
        }

        try:
            # Call the Transfer class to initiate a transfer and validate the response
            response = self.hydrogenpay.PaymentService.initiate(payment_details)
            # print(f"Payment initiation success: {response}")
            logger.info("Bank transfer initiated successfully:")
            logger.info(json.dumps(response, indent=4))


        except HydrogenpayExceptions.PaymentInitiateError as e:
            # Mark test as failed if payment initiation fails
            self.fail(f"Payment initiation failed: {e}")

```

*Arguments*

- `amount`: Amount to trasfer
- `currency`: Default to NGN if not passed, other currencies available are USD and GBP.
- `email`: Customer’s Email Address.
- `customerName`: Customer's name.
- `meta`: Customer's email address
- `callback`: Redirect URL after payment has been completed on the gateway.
- `isAPI`: Amount in kobo


*Returns*

Response Example:

```py

Bank transfer initiated successfully:
{
    "error": false,
    "message": "Initiate bank transfer successful",
    "data": {
        "transactionRef": "36934683_473281644c",
        "virtualAccountNo": "1811357132",
        "virtualAccountName": "HYDROGENPAY",
        "expiryDateTime": "2024-10-10 19:09:32",
        "capturedDatetime": null,
        "completedDatetime": null,
        "transactionStatus": "Pending",
        "amountPaid": 50,
        "bankName": "Access Bank"
    }
}

```



## ```Bank Transfer```

Simulate a Bank Transfer Transaction to test account transfer behavior for completing transactions. The response includes essential details such as transaction status. Use the transactionRef from the initiate transfer to complete the simulation."

*Usage*

```python

from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions
import logging #If Using Logging instead of print.

 # Mock data for simulating a bank transfer
        transfer_details = {
            "amount": "50",
            "currency": "NGN",
            "clientTransactionRef": "36934683_87087a9180"  # Replace with an actual reference
        }

        try:
            # Call the SDK to simulate the bank transfer
            response = self.hydrogenpay.BankTransfer.simulatetransfer(transfer_details)
            logger.info("Simulate bank transfer successful:")
            logger.info(json.dumps(response, indent=4))


        except HydrogenpayExceptions.TransactionValidationError as e:
            # Handle errors and mark the test as failed
            self.fail(f"Simulate bank transfer failed: {e}")

```

*Arguments*

- `amount`: The amount to be transferred.
- `currency`: The currency in which the transaction is being made..
- `clientTransactionRef`: A unique reference for the client’s transaction.

*Returns*

Response Example:

```py

Simulate bank transfer successful:
{
    "error": false,
    "orderId": "36934683_886923fa59",
    "message": "Operation Successful",
    "merchantRef": "36934683",
    "customerEmail": "bwitlawalyusuf@gmail.com",
    "transactionId": "94850000-d1b0-2648-4dda-08dce8bc64e0",
    "amount": "50.00",
    "description": null,
    "currency": "NGN",
    "merchantInfo": null,
    "paymentId": "success-success-success-474512713",
    "discountPercentage": 0,
    "callBackUrl": null,
    "isRecurring": false,
    "frequency": null,
    "serviceFees": null,
    "isBankDiscountEnabled": false,
    "bankDiscountValue": null,
    "vatFee": null,
    "vatPercentage": 0,
    "transactionMode": 0
}

```


## ```Recurring Payment```
Recurring Payment allows businesses to set up subscription-based payments.


*Usage*

```python

from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions
import logging #If Using Logging instead of print.


# Mock data for initiating a payment
        payment_details = {
            "amount": 50,
            "customerName": "Lawal",
            "email": "bwitlawalyusuf@gmail.com",
            "currency": "NGN", # Default to NGN if not passed, other currencies available are USD and GBP.
            "description": "test desc",
            "meta": "test meta",
            "callback": "https://webhook.site/43309fe4-a1f7-406d-afff-09e1cb12b9ec", #"https://example.com/callback"
            "frequency": 0, # Daily
            #   "frequency": 1, // Weekly
            #   "frequency": 2, // Monthly
            #   "frequency": 3, // Quarterly
            #   "frequency": 4, // Yearly
            #   "frequency": 5, // Disable auto debit.
            "isRecurring": true, # Indicates if the payment is recurring.
            "endDate": "2024-10-09T19:01:41.745Z" #End date for the recurring payment cycle in ISO 8601 format (e.g., 2024-10-29T19:01:41.745Z).
        }

        try:
            # Call the Transfer class to initiate a transfer and validate the response
            response = self.hydrogenpay.PaymentService.initiate(payment_details)
            # print(f"Payment initiation success: {response}")
            logger.info("Payment initiation successful:")
            logger.info(json.dumps(response, indent=4))


        except HydrogenpayExceptions.PaymentInitiateError as e:
            # Mark test as failed if payment initiation fails
            self.fail(f"Payment initiation failed: {e}")

```

*Arguments*

- `amount`: Amount to debit the customer.
- `currency`: Default to NGN if not passed, other currencies available are USD and GBP.
- `email`: Customer’s Email Address.
- `customerName`: Customer's name.
- `meta`: Customer's email address
- `callback`: Redirect URL after payment has been completed on the gateway.
- `frequency`: Frequency of recurring payment
- `isRecurring`: Indicates if the payment is recurring.
- `endDate`: End date for the recurring payment cycle in ISO 8601 format



*Returns*

Response Example:

```py
Payment initiation successful:
{
    "error": false,
    "validationRequired": true,
    "txRef": "36934683_71131c452e",
    "authUrl": "https://payment.hydrogenpay.com?transactionId=94850000-d1b0-2648-175f-08dce946623e&Mode=19289182"
}

```


## Testing

All SDK tests are implemented using Python's ```unittest``` module. They currently cover:

```hydrogenpay.PaymentService```
```hydrogenpay.ConfirmPayment```
```hydrogenpay.BankTransfer```
```hydrogenpay.Transfer```

```sh
Running the Tests

1. Navigate to the tests directory in your terminal.

2. You can run each test file separately using the following command:

python -m unittest test_initiate_payment.py
python -m unittest test_confirm_payment.py
python -m unittest test_initiate_bank_transfer.py
python -m unittest test_simulate_bank_transfer.py

3. Optional: Run All Tests at Once

If you want to run all tests in the tests directory together, you can use the following command:

python -m unittest discover -s tests

```

## Support

For more assistance with this SDK, reach out to the Developer Experience team via [email](mailto:support@hydrogenpay.com) or consult our documentation [here](https://docs.hydrogenpay.com/reference/api-authentication)


## Contribution

If you discover a bug or have a solution to improve the Hydrogen Payment Gateway for the WooCommerce plugin, we welcome your contributions to enhance the code.


Create a detailed bug report or feature request in the "Issues" section.

If you have a code improvement or bug fix, feel free to submit a pull request.

 * Fork the repository on GitHub

 * Clone the repository into your local system and create a branch that describes what you are working on by pre-fixing with feature-name.

 * Make the changes to your forked repository's branch. Ensure you are using PHP Coding Standards (PHPCS).

 * Make commits that are descriptive and breaks down the process for better understanding.

 * Push your fix to the remote version of your branch and create a PR that aims to merge that branch into master.
 
 * After you follow the step above, the next stage will be waiting on us to merge your Pull Request.


## License

By contributing to this library, you agree that your contributions will be licensed under its [MIT license](/LICENSE).
Copyright (c) Hydrogen.


## Hydrogenpay API References

- [Hydrogenpay Dashboard](https://dashboard.hydrogenpay.com/merchant/profile/api-integration)
- [Hydrogenpay API Documentation](https://docs.hydrogenpay.com/reference/api-authentication)