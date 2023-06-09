#!/usr/bin/python3
"""
module that Writes a class Rectangle
that defines a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    Private instance attribute:
        width:
            with property to retrieve it.
            with property setter to set it.
        height:
            with property to retrieve it.
            with property setter to set it.
    raise: (width, height)
        TypeError: exception must be integer.
        ValueError: exception must be non negative.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    # to retrieve property
    def width(self):
        return self.__width

    @width.setter
    # to set property
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    # to retrieve property
    def height(self):
        return self.__height

    @height.setter
    # to set property
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
