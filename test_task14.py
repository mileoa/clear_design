import unittest
import random
from typing import List

from task14 import quickSort


class QuickSortTests(unittest.TestCase):

    def test_regression(self) -> None:
        first_array: List[int] = [5, 2, 9, 1, 3, 6, 7]
        quickSort(first_array, 0, len(first_array) - 1)
        self.assertEqual(first_array, [1, 2, 3, 5, 6, 7, 9])

        second_array: List[int] = [5, 2, 9, 1, 3, 6, 7]
        quickSort(second_array, 2, 5)
        self.assertEqual(second_array, [5, 2, 1, 3, 6, 9, 7])

    def test_empty(self) -> None:
        empty_array: List[int] = []
        quickSort(empty_array, 0, len(empty_array) - 1)
        self.assertEqual(empty_array, [])

    def test_random(self) -> None:
        for repeat in range(1000):
            array: List[int] = list(range(random.randint(0, 100)))
            array_native_sorted: List[int] = array.copy()
            random.shuffle(array)
            quickSort(array, 0, len(array) - 1)
            self.assertEqual(array, array_native_sorted)

    def test_border(self) -> None:
        array: List[int] = [1]
        quickSort(array, 0, len(array) - 1)
        self.assertEqual(array, [1])


if __name__ == "__main__":
    unittest.main()
