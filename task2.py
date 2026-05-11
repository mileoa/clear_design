import unittest


class AverageCalculator:

    def calculate_average(self, numbers: list[int]):
        if len(numbers) == 0:
            raise ValueError("numbers can not be empty")
        total: int = 0
        count: int = 0
        for number in numbers:
            total += number
            count += 1
        return total / count


class TestAverageCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = AverageCalculator()

    def test_calculate_average(self):
        result = self.calculator.calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_calculate_average_single_element(self):
        result = self.calculator.calculate_average([42])
        self.assertEqual(result, 42.0)

    def test_calculate_average_negative_numbers(self):
        result = self.calculator.calculate_average([-10, -20, -30])
        self.assertEqual(result, -20.0)

    def test_calculate_average_mixed_numbers(self):
        result = self.calculator.calculate_average([-5, 0, 5])
        self.assertEqual(result, 0.0)

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_average([])


if __name__ == "__main__":
    unittest.main()
