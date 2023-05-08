import asyncio
import time

async def say_something(word,delay):
    print("executing coroutine one")
    print(f"The word passed is {word}")
    await asyncio.sleep(delay)
    print(f"The coroutine has finished executing")

async def caller():
    print(f"the time started is {time.strftime('%X')}")
    await say_something("hello",4)
    await say_something("world",5)
    print(f"the time end is {time.strftime('%X')}")

#asyncio.run(caller())

# runn concurrelntly using gather()

async def greetings():
    print("welcome")
    await asyncio.sleep(3)
    print("home")

async def main():
    start = time.time()
    await asyncio.gather(greetings(),greetings())
    end = time.time() - start
    print(f"{__name__} executed in {end} seconds")

asyncio.run(main())




