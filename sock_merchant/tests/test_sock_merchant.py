import sock_merchant
import inspect
import os
import sys
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
                             inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class test_sock_merchant(unittest.TestCase):
    default_vars = {"n": 9, "ar": [10, 20, 20, 10, 10, 30, 50, 10, 20]}

    def test_solve_odd(self):
        self.assertEqual(sock_merchant.solve_sock_merchant(
                         self.default_vars.get('n'),
                         self.default_vars.get('ar')), 3)
        print(f"{self.id()}")

    def test_solve_even(self):
        n = 8
        ar = [10, 20, 20, 10, 10, 30, 50, 10]
        self.assertEqual(sock_merchant.solve_sock_merchant(n, ar), 3)
        print(f"{self.id()}")

    def test_is_integer(self):
        self.assertIsInstance(sock_merchant.solve_sock_merchant(
                         self.default_vars.get('n'),
                         self.default_vars.get('ar')), type(0))
        print(f"{self.id()}")


if __name__ == '__main__':
    unittest.main()
