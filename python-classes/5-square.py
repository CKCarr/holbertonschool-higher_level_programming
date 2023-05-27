#!/usr/bin/python3
"""
Module creates a class(type) Square &
defines a 'Square' instance with optional 'size' attribute.
It iniitializes a private instance attribute 'size' defaulted to 0.
It handles Type and Value errors.
Gets the size of the square.
Sets the size of the square.
Public instance method: def area(self):
that returns the current square area
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
f size is equal to 0, print an empty line
"""


class Square:
    """ Defines a Square.
    Attributes: __size (int): The size of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size < 0.
    """

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # This invokes the setter

    @property
    def size(self):
        """
        Gets size of the square.
        Returns: int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args: value (int): The size of the square.
        Raises: TypeError: If size is not an int.
                ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns: int: The area of the square
        """
        return self.__size ** 2  # This invokes the getter

    def my_print(self):
        """
        prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        if self.__size is 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
