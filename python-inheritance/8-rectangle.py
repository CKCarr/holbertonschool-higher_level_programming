#!/usr/bin/python3
""" Module Writes a class Rectangle that inherits from BaseGeometry
    which has 2 public instance methods:
    area() and integer_validator()
    """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ Instantiates a Rectangle object.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
