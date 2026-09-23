from enum import Enum
from dataclasses import dataclass
from decimal import Decimal
#PART A - EXCEPTIONS
class OrderNotFoundError(Exception):
    pass


class InvalidOrderStateError(Exception):
    pass

#PART B ORDER STATUS

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"

#PART C ORDER
@dataclass
class Order:
    order_id: int
    customer_name: str
    amount: Decimal
    status: OrderStatus = OrderStatus.PENDING
    
    def __post_init__(self):
        if self.order_id <= 0:
            raise ValueError("Order id should be greater than 0")
        
        if not isinstance(self.customer_name , str):
            raise TypeError("Customer name must be a string")
        
        if not self.customer_name.strip():
            raise ValueError("customer_name cannot be empty")
        
        if self.amount <= 0:
            raise ValueError("Amount should be greater than 0")
        
        if not isinstance(self.status , OrderStatus):
            raise TypeError("status must be an OrderStatus")

# PART D REPOSITORY 

class OrderRepository:
    
    def __init__(self) -> None:
        self.orders: dict[int, Order] = {}
    
    def save(self, order: Order) -> Order:
        self.orders[order.order_id] = order
        return order

    def get_by_id(self, order_id: int) -> Order:
        if order_id not in self.orders:
            raise OrderNotFoundError(f"Order {order_id} not found")
        
        return self.orders[order_id]
            

# PART E - SERVICE

class OrderService:
    
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository
    
    def create_order(self, order_id: int, customer_name: str, amount: Decimal) -> Order:
        order = Order(order_id = order_id, customer_name = customer_name, amount = amount)
        return self.repository.save(order)
    
    def pay_order(self, order_id: int) -> Order:
        order = self.repository.get_by_id(order_id)
        if order.status != OrderStatus.PENDING:
            raise InvalidOrderStateError(f"Cannot pay order in {order.status.value} state")
        order.status = OrderStatus.PAID
        return order
        
            
    def cancel_order(self, order_id: int) -> Order:
        order = self.repository.get_by_id(order_id)
        if order.status != OrderStatus.PENDING:
            raise InvalidOrderStateError(f"Cannot cancel order in {order.status.value} state")
        order.status = OrderStatus.CANCELLED
        return order
        

#EXPECTED USECASE

repository = OrderRepository()
service = OrderService(repository)

order = service.create_order(
    101,
    "Alice",
    Decimal("500.00")
)

print(f"create {order.order_id} -> {order.status.name}")

paid_order = service.pay_order(101)

print(paid_order.status.value)

repository = OrderRepository()
service = OrderService(repository)

# Create
order = service.create_order(
    101,
    "Alice",
    Decimal("500.00")
)

print(order.status)

# Pay
paid_order = service.pay_order(101)
print(paid_order.status)

# Pay again → should fail
try:
    service.pay_order(101)
except InvalidOrderStateError as e:
    print(e)

# Missing order → should fail
try:
    service.pay_order(999)
except OrderNotFoundError as e:
    print(e)

# Another order
order = service.create_order(
    102,
    "Bob",
    Decimal("1000.00")
)

# Cancel
cancelled_order = service.cancel_order(102)
print(cancelled_order.status)

# Pay cancelled order → should fail
try:
    service.pay_order(102)
except InvalidOrderStateError as e:
    print(e)