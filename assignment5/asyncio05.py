import asyncio
from random import random

async def cook_rice():
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    return f'Rice is ready in {cook_time:.4f} seconds'

async def cook_noodle():
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    return f'Noodle is ready in {cook_time:.4f} seconds'

async def cook_curry():
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    return f'Curry is ready in {cook_time:.4f} seconds'

async def main():
    tasks = [cook_rice(), cook_noodle(), cook_curry()]
    done, _ = await asyncio.wait([asyncio.create_task(task) for task in tasks], return_when=asyncio.FIRST_COMPLETED)
    
    for task in done:
        print(task.result())

asyncio.run(main())
