#oops
from decimal import Decimal

class Employee:
    def __init__(self, name: str, salary: Decimal) -> None:
        if salary < 0:
            raise ValueError("Salary should be greater than 0")
        
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        if not name.strip():
            raise ValueError("Name can not be empty")
        
        self.__name: str = name
        self.__salary: Decimal = salary
    
    @property
    def name(self) -> str:
        return self.__name
    @property
    def salary(self) -> Decimal:
        return self.__salary
    
    def calculate_bonus(self) -> Decimal:
        raise NotImplementedError

    

class Developer(Employee):
    
    def calculate_bonus(self) -> Decimal:
        bonus = self.salary*Decimal("0.10")
        return bonus


class Manager(Employee):
    
    def calculate_bonus(self) -> Decimal:
            bonus = self.salary*Decimal("0.20")
            return bonus

def calculate_total_compensation(employee:Employee) -> Decimal:
    return employee.salary + employee.calculate_bonus()


developer = Developer("Alice", Decimal("100000"))
manager = Manager("Bob", Decimal("120000"))

print(calculate_total_compensation(developer))
print(calculate_total_compensation(manager))

employees = [
    Developer("Alice", Decimal("100000")),
    Manager("Bob", Decimal("120000")),
    Developer("Charlie", Decimal("80000")),
    Manager("David", Decimal("150000")),
]

for employee in employees:
    print(f"{employee.name}, {calculate_total_compensation(employee)}")