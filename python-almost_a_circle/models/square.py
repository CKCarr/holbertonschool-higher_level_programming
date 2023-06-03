#!/usr/bin/python3
""" This module writes the class Square that inherits from Rectangle class.
Rectangle inherits from Base class.
base class has public instance attribute: ''id'' """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class.
    **As reminder: a Square is a Rectangle with the same width and height**
        """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the Square class that
        inherits from Rectangle class.
            Args:
            size (int): The size of the square (width and height).{EQUAL}
            x (int): The x-coordinate of the square. Defaults to 0.
            y (int): The y-coordinate of the square. Defaults to 0.
            id (int, optional): An identifier for the square.
            If not provided, it will be generated automatically.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading the __str__ method for the Square class.
            Returns: A string representation of a Square instance.
            [Square] (<id>) <x>/<y> - <size>
            **size can be width or height they are equal**
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )
