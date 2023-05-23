#!/usr/bin/python3
import unittest
from module_where_max_integer_is import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])


if __name__ == '__main__':
    unittest.main()
