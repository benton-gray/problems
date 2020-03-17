import repeated_string
import inspect
import os
import sys
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
                             inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class test_repeated_string(unittest.TestCase):
    default_vars = {"n": 10, "string": "aba"}

    def test_solve(self):
        self.assertEqual(repeated_string.solve_repeated_string(
                         self.default_vars.get('n'),
                         self.default_vars.get('string')), 7)
        print(f"{self.id()}")


if __name__ == '__main__':
    unittest.main()
