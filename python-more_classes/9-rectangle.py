#!/usr/bin/python3
"""
module that Writes a class Rectangle
that defines a rectangle
"""


class Rectangle:
    """ defines a rectangle
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
    Public instance method:
        area(int) - return: the rectangle area.
        perimeter(int) - return: the rectangle perimeter
            perimeter equals zero if width or height is equal to 0.
    Public class attribute number_of_instances:
    Initialized to 0
    Incremented during each new instance instantiation
    Decremented during each instance deletion
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = str(self.print_symbol) * self.__width + "\n"
        rectangle *= self.__height
        return rectangle

        """ method that prints representation of the Rectangle """
    def __repr__(self):
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
