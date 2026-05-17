# Состояние гонки, Итоговое значение счетчика может быть неверным из-за того что происходит состояние гонки, когда несколько потоков одновременно изменяют перменную и созраняют это значение из-за чего часть изменений теряется.
# deadlock. thread1 получает доступ к ресрусу 1 и ждет 50 милисекунд. После чего пытается получить доступ к ресурсу 2, не отпустив ресрус 1. Одновременно с этим thread2 успешно получает ресурс 2 до того как thread1 получил этот ресурс. И не отпустив этот ресрус пытается получить доступ к ресурсу 1, который уже знаят thread1. Из-за этого получается бесконечное ожидание.


import threading
import time


class RaceConditionExample:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def increment_counter(self):
        for _ in range(100000):
            with self.lock:
                self.counter += 1

    def main(self):
        number_of_threads = 10
        threads = []

        for i in range(number_of_threads):
            thread = threading.Thread(target=self.increment_counter)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Final counter value: {self.counter}")


class DeadlockExample:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()

    def thread1_task(self):
        with self.lock1:
            print("Thread 1 acquired lock1")

            time.sleep(0.05)

            with self.lock2:
                print("Thread 1 acquired lock2")

    def thread2_task(self):
        with self.lock1:
            print("Thread 2 acquired lock1")

            time.sleep(0.05)

            with self.lock2:
                print("Thread 2 acquired lock2")

    def main(self):
        thread1 = threading.Thread(target=self.thread1_task)
        thread2 = threading.Thread(target=self.thread2_task)

        thread1.start()
        thread2.start()

        try:
            thread1.join()
            thread2.join()
        except Exception:
            pass

        print("Finished")


if __name__ == "__main__":
    example = RaceConditionExample()
    example.main()
    example = DeadlockExample()
    example.main()
