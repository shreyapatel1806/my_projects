def devider(name , chapter):
    length = f"{name} is reading program {chapter}"
    print("\n")
    print(length)
    print("=" * len(length))



devider("Python", 1)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        elif amount == 0:
            raise ValueError("Amount must be greater than zero")
        elif amount >= 10000:
            raise ValueError("Amount must not exceed 10,000")
        self._balance += amount
    def get_balance(self):
        return self._balance
account = BankAccount(1000)
account.deposit(1000)
print(account.get_balance())



devider("Python", 2)
import asyncio
async def get_customer():
    await asyncio.sleep(2)
    return "Amit"
async def main():
    customer = await get_customer()
    print(customer)
asyncio.run(main())



devider("Python", 3)
from pydantic import BaseModel
class Customer(BaseModel):
    name: str
    age: int
    email: str

customer = Customer(
    name="Amit",
    age= 25, 
    email="shreya@gmail.com"
)

print(customer)
print("\n")