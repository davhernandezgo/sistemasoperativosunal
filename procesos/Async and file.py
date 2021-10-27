import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def read():
    fichero = open('datos.txt')
    lineas = fichero.readlines()
    for linea in lineas:
        print(linea)
        await sleep()

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        with open('datos.txt', 'a') as f:
            f.write(f'Task {name}: Computing {total}+{number}\n')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(read()),
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')