import unittest
import random


class GradeCalculator:
    def calculate_average(self, grades: list[int]):
        MAX_GRADE_ALLOWED: int = 5
        grades_amount: int = len(grades)
        if grades_amount == 0:
            raise ValueError("grades can not be empty")
        grades_sum: int = 0
        for grade in grades:
            if grade > MAX_GRADE_ALLOWED:
                raise ValueError(f"grade can not be > {MAX_GRADE_ALLOWED}")
            if grade <= 0:
                raise ValueError("grade can not be <= 0")
            grades_sum += grade
        return grades_sum / grades_amount


class TestGradeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = GradeCalculator()

    # 1 тип проверка обычных значений
    def test_calculate_average(self):
        result = self.calculator.calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    # 2 тип проверка пустого значения
    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_average([])

    # 3 тип проверка случайных значений
    def test_calculate_average_random(self):
        for i in range(1000):
            elements_amount: int = random.randint(0, 100)
            if elements_amount == 0:
                with self.assertRaises(ValueError):
                    self.calculator.calculate_average([])
                continue
            elements = []
            for k in range(elements_amount):
                elements.append(random.randint(-10, 10))
            result = self.calculator.calculate_average(elements)
            self.assertEqual(result, sum(elements) / len(elements))

    # 4 тип проверка корректности данных
    def test_calculate_average_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_average([-1, 5, 4])

    def test_calculate_average_big_numbers(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_average([1, 1, 6])

    # 5 тип проверка 1 значения
    def test_calculate_average_single_element(self):
        result = self.calculator.calculate_average([42])
        self.assertEqual(result, 42.0)


if __name__ == "__main__":
    unittest.main()
