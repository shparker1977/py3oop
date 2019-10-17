import asyncio

async def countdown(identifier, n):
    while n >0:
        print('left:', n, '({})'.format(identifier))
        await asyncio.sleep(1)
        n -=1

async def main():
    await asyncio.wait([
        countdown("A", 2),
        countdown("B", 3)
    ])