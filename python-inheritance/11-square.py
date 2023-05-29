#!/usr/bin/python3
""" Module writes a class Square that inherits from Rectangle
Rectangle has a height and width attribute and
has a method to calculate area.
Also it initializes a string definition of the Rectangle.
rectangle inherits from BaseGeometry which has
a integer_validator method as well as
an uninitialized area method """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square that inherits from Rectangle

    Args:
        Rectangle (int): The parent class given as base.
    """

    def __init__(self, size):
        """
        instantialize a square:
        with private attribute size:
        size must be a positive integer
        Rectangle is initialized with width and height.
        we call the super() in square instance to inherit
        and to initialize size as both width, height args.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ method calculates the area of a square """
        return self.__size ** 2

    def __str__(self):
        """
        Defines the string representation of a Square.
        Returns: (str) The Square description. """
        return f"[Square] {self.__size}/{self.__size}"
