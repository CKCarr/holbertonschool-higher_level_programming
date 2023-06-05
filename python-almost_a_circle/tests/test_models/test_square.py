#!/usr/bin/python3
""" This module is a unittest for the Square class """

import unittest
import os
import io
import sys

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test class for Square class """
    def setUp(self):
        """Set up test method"""
        # reset __nb_objects to 0 before each test
        print("Square setUp")
        Square._Base__nb_objects = 0

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.square = Square(1)

    def tearDown(self):
        """Tear down test method"""
        print("Square tearDown")

        sys.stdout = sys.__stdout__

        del self.square
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
