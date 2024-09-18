import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int, cashier_totals: dict):
    while True:
        customer: Customer = await queue.get()
        if customer is None:
            break 
        
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")

        total_time = 0
        for product in customer.products:
            print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}'s "
                  f"Product {product.product_name} for {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
            total_time += product.checkout_time

        print(f"The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} "
              f"in {round(total_time, 2)} secs")
        cashier_totals[cashier_number] += total_time
        queue.task_done()

def generate_customer(customer_id: int) -> Customer:
    all_products = [
        Product('beef', 1.0),
        Product('banana', 0.4),
        Product('sausage', 0.4),
        Product('diapers', 0.2)
    ]
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, number_of_customers: int):
    for customer_id in range(number_of_customers):
        customer = generate_customer(customer_id)
        print(f"Waiting to put Customer_{customer.customer_id} in line....")
        await queue.put(customer)
        print(f"Customer_{customer.customer_id} put in line...")
        await asyncio.sleep(0.01)  

    for _ in range(3):  
        await queue.put(None)

async def main():
    customer_queue = Queue()
    customers_count = 2  
    customers_start_time = time.perf_counter()
    cashier_totals = {0: 0, 1: 0, 2: 0}

    await customer_generation(customer_queue, customers_count)
    cashiers = [checkout_customer(customer_queue, i, cashier_totals) for i in range(3)]

    await asyncio.gather(*cashiers)
    print("\n--------------------------")
    for cashier, total_time in cashier_totals.items():
        if total_time > 0:
            print(f"The Cashier_{cashier} took {round(total_time, ndigits=2)} secs.")
    
    print(f"\nThe supermarket process finished in {round(time.perf_counter() - customers_start_time, 2)} secs")

if __name__ == "__main__":
    asyncio.run(main())