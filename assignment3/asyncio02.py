# example of running a coroutine
import asyncio

# Define a coroutine
async def custom_coro():
    # Await another coroutine
    await asyncio.sleep(1)

# Main coroutine
async def main():
    # Execute my custom coroutine
    await custom_coro()

# Check the type of the coroutine
asyncio.run(main())