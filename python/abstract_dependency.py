#Abstract Base Classes + Dependency Injection

from abc import ABC, abstractmethod
from decimal import Decimal

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: Decimal) -> str:
        ...

class MockPaymentGateway(PaymentGateway):
    
    def charge(self, amount: Decimal) -> str:
        if amount <= 0:
            raise ValueError("amount should be greater than 0")
        print(f"Processing mock payment: {amount}")
        return "mock_txn_123"

class StripePaymentGateway(PaymentGateway):
    
    def charge(self, amount: Decimal) -> str:
            if amount <= 0:
                raise ValueError("amount should be greater than 0")
            
            print(f"Processing stripe payment: {amount}")
            return "stripe_txn_123"

class PaymentService :
    
    def __init__(self, gateway: PaymentGateway) -> None:
        self.gateway = gateway

    def process_payment(self, amount: Decimal) -> str:
        return self.gateway.charge(amount)

mock_gateway = MockPaymentGateway()

payment_service = PaymentService(mock_gateway)

transaction_id = payment_service.process_payment(
    Decimal("500.00")
)

print(transaction_id)

stripe_gateway = StripePaymentGateway()

payment_service = PaymentService(stripe_gateway)

transaction_id = payment_service.process_payment(
    Decimal("500.00")
)

print(transaction_id)