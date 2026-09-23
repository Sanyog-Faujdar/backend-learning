# dataclass + Enum
# dataclass → structure/model for the order
# Enum → controlled set of valid order statuses
# Decimal → correct representation for money

from enum import Enum
from decimal import Decimal
from dataclasses import dataclass

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

@dataclass
class Order:
    order_id: int
    customer_name: str
    amount: Decimal
    status: OrderStatus
    
    def __post_init__(self):
        if self.order_id <= 0:
            raise ValueError("order_id must be greater than 0")
        
        if not isinstance(self.customer_name, str):
            raise TypeError("customer_name must be a string")

        if not self.customer_name.strip():
            raise ValueError("customer_name cannot be empty")
        
        if self.amount < 0:
            raise ValueError
        
        if not isinstance(self.status, OrderStatus):
            raise TypeError("status must be an OrderStatus")
    
    def is_completed(self) -> bool:
        return self.status in (OrderStatus.PAID, OrderStatus.SHIPPED)

order = Order(
    order_id=101,
    customer_name="Alice",
    amount=Decimal("2500.00"),
    status=OrderStatus.PAID
)

print(order)
print(order.status.value)
print(order.is_completed())

# Order(0, "Alice", Decimal("100"), OrderStatus.PAID)

# Order(101, "   ", Decimal("100"), OrderStatus.PAID)

# Order(101, "Alice", Decimal("-100"), OrderStatus.PAID)

Order(101, "Alice", Decimal("100"), "paid")