import twod_array
import inspect
import os
import sys
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
                             inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class test_twod_array(unittest.TestCase):
    default_vars = {"n": 10, "string": "aba"}

    def test_solve(self):
        self.assertEqual(twod_array.solve_twod_array(
                         self.default_vars.get('n'),
                         self.default_vars.get('string')), 7)
        print(f"{self.id()}")


if __name__ == '__main__':
    unittest.main()
