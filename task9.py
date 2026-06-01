import random
from concurrent.futures import ThreadPoolExecutor


class ComplexMultiThreadProcessing:
    def __init__(self):
        self._size: int = 1000000
        self._threads_amount: int = 4
        self._data: list[int] = []
        self._sum: int = 0

    def main(self):
        self._data: list[int] = [random.randint(0, 99) for _ in range(self._size)]
        chunk_size: int = self._size // self._threads_amount
        chunk_bounds = [
            (i * chunk_size, (i + 1) * chunk_size) for i in range(self._threads_amount)
        ]
        with ThreadPoolExecutor(max_workers=self._threads_amount) as executor:
            result_sums = executor.map(
                lambda bounds: sum(self._data[bounds[0] : bounds[1]]),
                chunk_bounds,
            )
            total_sum: int = sum(result_sums)
        self._sum = total_sum
        print(self._sum)


if __name__ == "__main__":
    complex_multy = ComplexMultiThreadProcessing()
    complex_multy.main()
