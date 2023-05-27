#!/usr/bin/python3
""" The module creates a class that defines a 'Square'
    Initializes a private instance attribute 'size'
    This module handles TypeErrors and ValueErrors.
    Initializes a public instance method 'def area(self):'
    Returns: the current square area """


class Square:
    """ Class: Creates type Square.
        Definition: represents a square.
        Attribute: __size(int): The size of the square, Defaults to 0
    """
    def __init__(self, size=0):
        """ Constructs a Square instance.
        Args: __size (int, optional): the size of the Square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the area of the Square
        Returns:
            int: the area of the square
        """
        return self.__size ** 2
