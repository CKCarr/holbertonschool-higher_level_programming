#!/usr/bin/python3


""" Write the class Rectangle that inherits from Base."""


# Import the Base class
from models.base import Base


class Rectangle(Base):
    """ Constructor of the Rectangle class that inherits from Base class.

    Args:
        Base (class): The class to inherit from.
            Base: public instance attribute: ''id''
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of the Rectangle class that inherits from Base class.
        Parameters:
        Call the super class with id: super().__init__(id)
        id (int, optional): id of the instance (inherited from Base)
        Private instance attributes:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int): horizontal offset (default 0)
            y (int): vertical offset (default 0) """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# Getters and Setters
    @property
    def width(self):
        """ Getter for the private instance attribute:
                'width' of the Rectangle.
            Returns:
                The width of the Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the __width of the Rectangle.
            Args:
                value (int): The width of the Rectangle. """
        self.__width = value

    @property
    def height(self):
        """ Getter for the private instance attribute:
                'height' of the Rectangle.
            Returns:
                The height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the __height of the Rectangle
            Args:
                value (int): The height of the Rectangle. """
        self.__height = value

    @property
    def x(self):
        """ Getter for the private instance attribute: 'x' of the Rectangle.
            Returns:
                The x of the Rectangle. (horizontal offset) """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x (horizontal offset) of the Rectangle. """
        self.__x = value

    @property
    def y(self):
        """ Getter for the private instance attribute y (vertical offset) of
        the Rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the private instance attribute y (vertical offset) of
        the Rectangle. """
        self.__y = value

# Public Methods
