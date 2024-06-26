# check the type of a coroutine
import asyncio

# Define a coroutine
async def custom_coro():
    # Await another coroutine
    await asyncio.sleep(1)

# Create the coroutine
coro = custom_coro()

# Check the type of the coroutine
print(type(coro))