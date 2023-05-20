#!/usr/bin/python3
""" class Square that defines a square.
    Private instance attribute: size.
        property def size(self): to retrieve it.
        property setter def size(self, value): to set it:
        must be an integer, otherwise raise a TypeError.
        if size is less than 0, raise a ValueError.
    Private instance attribute: position:
        property def position(self): to retrieve it.
        property setter def position(self, value): to set it:
        position must be a tuple of 2 positive integers,
        otherwise raise a TypeError.
    Instantiation with optional size and optional position:
        def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
        that returns the current square area.
    Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line.
    position should be use by using space
    - Don’t fill lines by spaces when position[1] > 0
"""


class Square:
    """Defines a square with a size and a position """

    def __init__(self, size=0, position=(0, 0)):
        """ initializes the square.

        Args:
            size (int, optional): size of the sq.
            Defaults to 0.

            position (tuple, optional): tuple of two positive integers
            represent position of square in 2D,
            position[0]=horizontal - position[1]=vertical.
            Defaults to (0, 0).
        """
        self.size = size  # Invokes the setter
        self.position = position  # Invokes the setter

    @property
    def size(self):
        """ Gets the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, validates the input.
        Args:
            value (int): The size of the square.
            Must be a positive integer.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Gets the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position of the square, validates the input

        Args:
            value (int): position must be a tuple of 2 positive ints,
            otherwise raise a TypeError.
        """
        if (type(value) is not tuple or len(value) != 2 or
           not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the are of the square """
        return self.size * self.size  # Invokes the getter

    def my_print(self):
        """Prints the square using the # symbol at its position."""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print("\n".join(" " * self.position[0] + "#" * self.size
                            for _ in range(self.size)))
