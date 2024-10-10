<p align="center">
    <img title="Hydrogen" height="200" src="https://hydrogenshared.blob.core.windows.net/shared/hydrogen-logo2.png" width="50%"/>
</p>

# Hydrogen Python

## Introduction

The Python library facilitates seamless payments via card transactions and account transfers, ensuring faster delivery of goods and services. 
Seamlessly integrate Hydrogen APIs with Flask, Django, and other Python applications. Our library simplifies direct integration, enabling rapid and efficient API requests.


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
6. [Contribution guidelines](#)
7. [License](#)


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
Response OK: 2.92565s
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
            logger.info("Transfer initiated successful:")
            logger.info(json.dumps(response, indent=4))


        except HydrogenpayExceptions.PaymentInitiateError as e:
            # Mark test as failed if payment initiation fails
            self.fail(f"Payment initiation failed: {e}")

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









## Testing

All of the SDK's tests are written with Python's ```unittest``` module. The tests currently test:
```rave.Account```
```rave.Card```
```rave.Transfer```
```rave.Preauth```
```rave.Subaccount```
```rave.Subscriptions```
```rave.Paymentplan```

They can be run like so:

```sh
python test.py
```

>**NOTE:** If the test fails for creating a subaccount, just change the ```account_number``` ```account_bank```  and ```businesss_email``` to something different

>**NOTE:** The test may fail for account validation - ``` Pending OTP validation``` depending on whether the service is down or not
<br>


## Debugging Errors
We understand that you may run into some errors while integrating our library. You can read more about our error messages [here](https://developer.flutterwave.com/docs/integration-guides/errors).

For `authorization` and `validation` error responses, double-check your API keys and request. If you get a `server` error, kindly engage the team for support.



## Support
For additional assistance using this library, contact the developer experience (DX) team via [email](mailto:developers@flutterwavego.com) or on [slack](https://bit.ly/34Vkzcg). 

You can also follow us [@FlutterwaveEng](https://twitter.com/FlutterwaveEng) and let us know what you think 😊.


## Contribution guidelines
Read more about our community contribution guidelines [here](/CONTRIBUTING.md)


## License

By contributing to this library, you agree that your contributions will be licensed under its [MIT license](/LICENSE).
Copyright (c) Flutterwave Inc.

## Test section
Sample Description for teset file. 

Final test 3 out of 10. Fingers crossed
