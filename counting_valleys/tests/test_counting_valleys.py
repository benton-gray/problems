import counting_valleys
import inspect
import os
import sys
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
                             inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class test_counting_valleys(unittest.TestCase):
    default_vars = {"n": 8, "ar": "UDDDUDUU"}

    def test_solve_odd(self):
        n = 9
        ar = "UDDDUDUUU"
        self.assertEqual(counting_valleys.solve_counting_valleys(n, ar), 1)
        print(f"{self.id()}")

    def test_solve_even(self):
        self.assertEqual(counting_valleys.solve_counting_valleys(
                         self.default_vars.get('n'),
                         self.default_vars.get('ar')), 1)
        print(f"{self.id()}")

    def test_is_integer(self):
        self.assertIsInstance(counting_valleys.solve_counting_valleys(
                         self.default_vars.get('n'),
                         self.default_vars.get('ar')), type(0))
        print(f"{self.id()}")


if __name__ == '__main__':
    unittest.main()
