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



devider("Python", 9)
import asyncio
async def get_customer():
    await asyncio.sleep(2)
    return "Amit"
async def get_orders():
    await asyncio.sleep(3)
    return "Orders"
async def main():
    customer, orders = await asyncio.gather(
        get_customer(),
        get_orders()
    )
    print(customer)
    print(orders)
asyncio.run(main())



devider("Python", 10)
import asyncio


async def get_customer():
    await asyncio.sleep(2)
    return "Customer data"


async def get_orders():
    await asyncio.sleep(3)
    return "Order data"


async def main():
    customer, orders = await asyncio.gather(
        get_customer(),
        get_orders()
    )

    print(customer)
    print(orders)


asyncio.run(main())


devider("Python", 11)
import asyncio

async def get_customer():
    await asyncio.sleep(2)
    return "Customer data"

async def get_orders():
    await asyncio.sleep(3)
    return "Order data"

async def get_payments():
    await asyncio.sleep(1)
    return "Payment data"

async def get_inventory():
    await asyncio.sleep(4)
    return "Inventory data"

async def load_dashboard():
    customer, orders, payments, inventory = await asyncio.gather(
        get_customer(),
        get_orders(),
        get_payments(),
        get_inventory()
    )
    print(customer)
    print(orders)   
    print(payments)
    print(inventory)
    print("Dashboard loaded successfully")

    # return {
    #     "customer": customer,
    #     "orders": orders,
    #     "payments": payments,
    #     "inventory": inventory
    # }



asyncio.run(load_dashboard())



devider("Python", 12)
import asyncio


async def get_customer():
    await asyncio.sleep(1)
    raise ValueError("Customer service failed")


async def main():
    try:
        customer = await get_customer()
        print(customer)

    except ValueError as error:
        print(f"Error: {error}")


asyncio.run(main())



devider("Python", 13)
import asyncio


async def call_service():
    await asyncio.sleep(5)
    return "Success"


async def main():
    try:
        result = await asyncio.wait_for(
            call_service(),
            timeout=2
        )
        print(result)

    except asyncio.TimeoutError:
        print("Service took too long")


asyncio.run(main())



devider("Python", 14)
import asyncio
async def call_api():
    await asyncio.sleep(1)
    return "Success"
async def call_with_retry():
    for attempt in range(3):
        try:
            return await call_api()
        
        except Exception:
            if attempt == 3:
                raise
            await asyncio.sleep(1)

asyncio.run(call_with_retry())





devider("Python", 15)
import asyncio
async def async_http_request(url):
    await asyncio.sleep(2)
    return f"Response from {url}"

async def fetch_customer():
    response = await async_http_request(
        "https://www.youtube.com/"
    )

    # return response
    print(response)


asyncio.run(fetch_customer())



devider("Python", 16)

import asyncio
async def task_a():
    await asyncio.sleep(5)
    print("A done")


async def task_b():
    await asyncio.sleep(1)
    print("B done")

async def main():
    await asyncio.gather(
        task_a(),
        task_b()
    )

asyncio.run(main())