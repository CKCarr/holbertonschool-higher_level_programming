#!/usr/bin/python3
"""Module containing the definition for class 'BaseGeometry'.
Public instance method: def area(self):
Raises:  Exception: with the message "area() is not implemented"
"""


class BaseGeometry:
    """A class called 'BaseGeometry' that contains an unimplemented method."""

    def area(self):
        """ Function Raises an exception when called.
        indicating that this method has not yet been implemented.
        """
        raise Exception("area() is not implemented")
