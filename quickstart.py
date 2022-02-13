import asyncio
import time


async def main():
    print(f"{time.ctime()} Hello, world!")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Hello, again!")


def blocking():
    print(f"{time.ctime()} Hello, from thread!")
    time.sleep(1)
    print(f"{time.ctime()} Hello, again thread!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
