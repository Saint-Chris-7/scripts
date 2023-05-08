# coroutine is an awaitable object
import asyncio

async def mul(first:int,second:int) ->int:
    print("calculating  multiplication")
    await asyncio.sleep(2)
    result = first * second
    print(f"{first} multiplied by {second}")
    return result

async def add(first:int,second:int):
    print("addition of two numbers")
    await asyncio.sleep(3)
    result = first + second
    print(f"{first} is added to {second}")
    return result    

async def main(first, second):
    await asyncio.gather(mul(first,second),add(first,second))
    await asyncio.create_task(mul(first,second))
    await asyncio.create_task(add(first,second))
    # await mul(first,second)
    # await add(first,second)

asyncio.run(main(8,9))