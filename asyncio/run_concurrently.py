# runnning the coroutine concurrently
import asyncio
import time

async def say_something(word,delay):
    print("executing coroutine one")
    print(f"The word passed is {word}")
    await asyncio.sleep(delay)
    print(f"The coroutine has finished executing")

async def caller():
    print(f"the time started is {time.strftime('%X')}")
    
    await asyncio.create_task(say_something("chris",2))
    await asyncio.create_task(say_something("world",5))

    print(f"the time end is {time.strftime('%X')}")

asyncio.run(caller())
