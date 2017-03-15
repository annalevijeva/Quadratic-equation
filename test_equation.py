import unittest
from equation import equation


# class EquationTestCase(unittest.TestCase):
#     def test_equation(self):
#         result = equation(-2, 1, 1)
#         self.assertEqual(result, equation(-2, 1, 1))

class EquationTestCase(unittest.TestCase):
    def test_solves_equation(self):
        """Solve y=1*(x**2) + 0*x - 4"""
        solution = {2, -2}  # {-2, 2} = {2, -2}
        result = equation(1, 0, -4)
        self.assertEqual(solution, result)
