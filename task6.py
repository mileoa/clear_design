from uuid import uuid4
from threading import Semaphore, Lock
from random import randint
import asyncio
from datetime import datetime
from multiprocessing import Process as mp_Process, Value, Lock
import threading
import time


# Мьютекс/блокировка
class Account:
    def __init__(self):
        self._amount: int = 0
        self._mutex = asyncio.Lock()

    async def deposit(self, amount):
        async with self._mutex:
            await asyncio.sleep(0.1)
            print(f"Deposit {amount} {datetime.now()}")
            self._amount += amount

    async def withdraw(self, amount):
        async with self._mutex:
            await asyncio.sleep(0.1)
            print(f"Withdraw {amount} {datetime.now()}")
            self._amount -= amount

    async def get_amount(self):
        return self._amount


async def mutex_show():
    account = Account()
    tasks = [account.deposit(50) for _ in range(10)] + [
        account.withdraw(30) for _ in range(3)
    ]
    await asyncio.gather(*tasks)
    balance = await account.get_amount()
    print(f"Итоговый баланс: {balance}")
    print("Ожидаемый: 410")


# Семафор
class RequestLimiter:
    def __init__(self, max_requests=1):
        self._request: str = {}
        self._response: str = {}
        self._max_requests: int = max_requests
        self._semaphore = asyncio.Semaphore(self._max_requests)

    async def get(self, request_id, request):
        async with self._semaphore:
            self._request[request_id] = request
            print(f"Put answer for {request_id} {datetime.now()}")
            await asyncio.sleep(1)
            self._response[request_id] = "answer"
            print(f"Got answer for {request_id} {datetime.now()}")


async def semaphore_show():
    request_limiter = RequestLimiter(2)
    tasks = [request_limiter.get(id, f"request {id}") for id in range(10)]
    await asyncio.gather(*tasks)


# Barrier
class Process:
    def __init__(self, workers_amount):
        self.barrier = asyncio.Barrier(workers_amount)

    async def prepare(self, id):
        print(f"Worker {id}: prepare begin")
        await asyncio.sleep(1)
        print(f"Worker {id}: prepare done")
        await self.barrier.wait()

    async def send(self, id):
        print(f"Worker {id}: send begin")
        await asyncio.sleep(1)
        print(f"Worker {id}: send done")
        await self.barrier.wait()

    async def close(self, id):
        print(f"Worker {id}: close begin")
        await asyncio.sleep(1)
        print(f"Worker {id}: close done")


async def worker(process, process_id):
    await process.prepare(process_id)
    await process.send(process_id)
    await process.close(process_id)


async def barrier_show():
    process = Process(3)
    tasks = [worker(process, i) for i in range(3)]
    await asyncio.gather(*tasks)


# Атомарные операции
def atomic_show():
    counter = Value("i", 0)
    lock = Lock()

    processes = [
        mp_Process(target=increment_counter, args=(counter, lock)) for _ in range(1000)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Результат {counter.value}")


def increment_counter(counter, lock):
    with lock:
        counter.value += 1


# Event
def event_show():
    event = threading.Event()
    threads = []
    for i in range(3):
        t = threading.Thread(
            target=worker_event,
            args=(
                event,
                f"Поток {i+1}",
            ),
        )
        t.start()
        threads.append(t)
    time.sleep(2)
    event.set()

    for t in threads:
        t.join()


def worker_event(event, name):
    print(f"{name} wait event")
    event.wait()
    print(f"{name} got event")


async def main():
    await semaphore_show()
    await mutex_show()
    await barrier_show()


if __name__ == "__main__":
    asyncio.run(main())
    atomic_show()
    event_show()
