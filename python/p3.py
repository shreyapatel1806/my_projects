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
from pydentic import BaseModel
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



devider("Python", 4)
from pydantic import BaseModel, Field
class Order(BaseModel):
   customer_id: int
   amount: float = Field(gt=0)
print(Order(customer_id=101 , amount = 500))



devider("Python", 5)
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
def test_calculate_total():
    result = calculate_total(100, 3)
    assert result == 300
    print("Test passed: calculate_total(100, 3) == 300")

test_calculate_total()



devider("Python", 6)
import pytest 

def calculate_discount(price: float, discount: float) -> float:
    if price < 0:
        raise ValueError("Price must be non-negative")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")      

    return price - (price * discount / 100)

def test_discount():
    assert calculate_discount(100, 10) == 90
    print("Test passed: calculate_discount(100, 10) == 90")

def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)
    print("Test passed: calculate_discount(-100, 10) raises ValueError")  
test_discount()
test_invalid_price()



devider("Python", 7)
import logging
logging.basicConfig(level=logging.INFO)
logging.debug("Customer ID = 101")
logging.info("Order created successfully")
logging.warning("Payment retry required")
logging.error("Payment processing failed")
logging.critical("Database unavailable")



devider("Python", 8)
import logging

logging.basicConfig(level=logging.INFO)

try:
    age = input("Enter age: ")
    age = int(age)
    print("Age:", age)
except ValueError:
    logging.error("failed to convert age")