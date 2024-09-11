import time
import asyncio
async def strong_man(name, power):
    list = [1, 2, 3, 4, 5]
    for ball in list:
        print(f'Силач {name} начал соревнования')
        await asyncio.sleep(1/power)
        print(f'Силач {name}, поднял {ball}')
    print(f'Силач {name}, закончил соревнование')

async def start_tournament():
    a = asyncio.create_task(strong_man('nya', 5))
    b = asyncio.create_task(strong_man('not nya', 2))
    c = asyncio.create_task(strong_man('not not nya', 3))
    await a
    await b
    await c

asyncio.run(start_tournament())