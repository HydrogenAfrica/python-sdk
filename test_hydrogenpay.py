"""
How to Run the Test:
--------------------
1. Make sure you have Python's `unittest` module installed (it comes pre-installed with Python).
2. Ensure you have the required dependencies installed by running:
   pip install -r requirements.txt

3. To run the test, open a terminal and navigate to the directory where `test_hydrogenpay.py` is located.

4. Execute the following command:
   python -m unittest test_hydrogenpay.py

   This will run all the test cases in the file and display the results in the terminal.
"""

import unittest
from hydrogenpay_python import Hydrogenpay, HydrogenpayExceptions
from dotenv import load_dotenv
import os
import logging
import json

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class TestHydrogenpaySDK(unittest.TestCase):

    def setUp(self):
        
        """
        Set up the Hydrogenpay instance before each test.
        The API keys and environment mode (test/live) are loaded from environment variables.
        """
        mode = os.getenv("MODE")  # This will be either 'test' or 'live'

        # Set up the Hydrogenpay instance using API keys from environment variables and the mode
        self.hydrogenpay = Hydrogenpay(
            os.getenv("SANDBOX_API_KEY"),
            os.getenv("LIVE_API_KEY"),
            mode=mode  # Pass mode as a parameter
        )

    def test_initiate_payment(self):

        """
        Test Case 1: Tests the initiation of a payment transaction using mock data.
        The function checks for necessary response fields like validationRequired and authUrl.
        """
        # Mock data for initiating a payment
        payment_details = {
            "amount": "50",
            "currency": "NGN",
            "email": "bwitlawalyusuf@gmail.com",
            "customerName": "Lawal Yusuf",
            "meta": "Test Py transaction",
            "callback": "https://webhook.site/43309fe4-a1f7-406d-afff-09e1cb12b9ec",
            "isAPI": True
        }

        # Call the SDK initiate function and validate the response
        try:
            response = self.hydrogenpay.PaymentService.initiate(payment_details)

            # Log the formatted response instead of printing raw data
            # print(f"Payment initiation success: {response}")
            logger.info("Payment initiation success:")
            logger.info(json.dumps(response, indent=4))

            # Assertions
            self.assertIn("validationRequired", response)
            self.assertTrue(response["validationRequired"])
            self.assertIn("authUrl", response)
            self.assertIsNotNone(response["authUrl"])

        except HydrogenpayExceptions.PaymentInitiateError as e:
            self.fail(f"Payment initiation failed with error: {e}")



    def test_confirm_payment(self):

        """
        Test Case 2: Confirms the payment status of a previously initiated transaction.
        Uses a transaction reference to verify the payment status.
        """

        # Transaction reference obtained from a previous payment initiation
        txRef = "36934683_87087a9180"

        try:
            # Call the SDK to confirm the payment status
            response = self.hydrogenpay.PaymentService.confirmpayment(txRef)

            # Log the formatted response
            logger.info("Payment Confirmation Successful:")
            logger.info(json.dumps(response, indent=4))

            # Assertions
            # Validate the payment status
            self.assertEqual(response["status"], "Paid")

        except HydrogenpayExceptions.TransactionVerificationError as e:
            self.fail(f"Transaction Confirmation Failed: {e}")



    def test_initiate_bank_transfer(self):

        """
        Test Case 3: Initiates a bank transfer and validates the response structure.
        The test checks for important fields like transactionRef, virtualAccountNo, and bankName.
        """

        # Mock data for initiating a bank transfer
        transfer_details = {
            "amount": "50",
            "currency": "NGN",
            "email": "bwitlawalyusuf@gmail.com",
            "customerName": "Lawal Yusuf",
            "description": "Test Python Payment for services",
            "meta": "Test transfer",
            "callback": "https://webhook.site/43309fe4-a1f7-406d-afff-09e1cb12b9ec"
        }

        try:
            # Call the SDK to initiate a bank transfer
            response = self.hydrogenpay.Transfer.initiate(transfer_details)

            # Log the formatted response
            logger.info("Bank transfer initiation successful:")
            logger.info(json.dumps(response, indent=4))

            # Validate the response based on the expected structure
            self.assertEqual(response["error"], False)
            self.assertEqual(response["message"], "Initiate bank transfer successful")

            data = response.get("data", {})
            self.assertIn("transactionRef", data)
            self.assertIn("virtualAccountNo", data)
            self.assertIn("virtualAccountName", data)
            self.assertIn("expiryDateTime", data)
            self.assertEqual(data["transactionStatus"], "Pending")
            self.assertEqual(data["amountPaid"], 50)
            self.assertEqual(data["bankName"], "Access Bank")

        except HydrogenpayExceptions.TransactionValidationError as e:
            # Handle errors and mark the test as failed
            self.fail(f"Bank transfer initiation failed: {e}")



    def test_simulate_bank_transfer(self):

        """
        Test Case 4: Simulates a bank transfer using mock data and validates the response.
        The test checks for fields like orderId, merchantRef, transactionId, and amount.
        """

        # Mock data for simulating a bank transfer
        transfer_details = {
            "amount": "50",
            "currency": "NGN",
            "clientTransactionRef": "36934683_4460569283", # Ref from Initiate Transfer
        }

        try:
            # Call the SDK to simulate the bank transfer
            response = self.hydrogenpay.BankTransfer.simulatetransfer(transfer_details)

            # Log the formatted response
            logger.info("Simulate Bank transfer initiation successful:")
            logger.info(json.dumps(response, indent=4))

            # Validate the response based on the expected structure
            self.assertEqual(response["error"], False)
            self.assertEqual(response["message"], "Operation Successful")

            data = response
            self.assertIn("orderId", data)
            self.assertIn("merchantRef", data)
            self.assertIn("customerEmail", data)
            self.assertIn("transactionId", data)
            self.assertEqual(data["amount"], '50.00')
            self.assertIn("transactionMode", data)

        except HydrogenpayExceptions.TransactionValidationError as e:
            # Handle errors and mark the test as failed
            self.fail(f"Simulate Bank transfer initiation failed: {e}")

            


if __name__ == "__main__":
    unittest.main()
