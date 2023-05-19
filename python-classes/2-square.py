#!/usr/bin/python3
""" Write a class Square that defines a square by: size """


class Square:
    """ Private instance attribute: size """
    def __init__(self, size=0):
        """size must be an integer, otherwise raise a TypeError"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """ if size is less than 0, raise a ValueError exception """
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
