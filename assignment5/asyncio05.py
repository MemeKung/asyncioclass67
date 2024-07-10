import asyncio
from random import random

async def cook_rice():
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    return f'Rice is ready in {cook_time} seconds'

async def cook_noodle():
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    return f'Noodle is ready in {cook_time} seconds'

async def cook_curry():
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    return f'Curry is ready in {cook_time} seconds'

async def main():
    tasks = [asyncio.create_task(cook_rice(), name="Rice"), asyncio.create_task(cook_noodle(), name="Noodle"), asyncio.create_task(cook_curry(), name="Curry")]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for task in tasks:
        if not task.done():
            await task
        print(task.result())

    print(f'Completed task: {len(done)}') 

    for task in done:
        print(f'\t- Finished cooking: {task.get_name()}')

    print(f'Uncompleted task: {len(pending)}')

asyncio.run(main())
