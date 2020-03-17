import jumping_on_the_clouds
import inspect
import os
import sys
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(
                             inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class test_jumping_on_the_clouds(unittest.TestCase):
    default_vars = {"ar": [0, 0, 1, 0, 0, 1, 0]}

    def test_solve_odd(self):
        self.assertEqual(jumping_on_the_clouds.solve_jumping_on_the_clouds(
                         self.default_vars.get('ar')), 4)
        print(f"{self.id()}")

    def test_solve_even(self):
        ar = [0, 0, 0, 1, 0, 0]
        self.assertEqual(
            jumping_on_the_clouds.solve_jumping_on_the_clouds(ar), 3)
        print(f"{self.id()}")

    def test_is_integer(self):
        self.assertIsInstance(
            jumping_on_the_clouds.solve_jumping_on_the_clouds(
                self.default_vars.get('ar')), type(0))
        print(f"{self.id()}")


if __name__ == '__main__':
    unittest.main()
