#OOP:Bank Account
class BankAccount:
    def __init__(self,owner: str,initial_balance: int) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance can not be negative")
        if not owner :
            raise ValueError("Owner can not be empety")
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string")
        self.owner: str = owner
        self.__balance: int = initial_balance
    
    def deposit(self,amount: int) -> None :
        if amount<=0:
            raise ValueError(f"Deposit amount must be greater than 0")
        self.__balance += amount
    
    def withdraw(self,amount: int) -> None:
        if amount<=0:
            raise ValueError(f"withdraw amount must be greater than 0")
        if amount>self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
    
    @property
    def balance(self) -> int:
        return self.__balance

account = BankAccount("Saiam", 1000)

account.deposit(500)    
account.withdraw(300)

print(account.balance)