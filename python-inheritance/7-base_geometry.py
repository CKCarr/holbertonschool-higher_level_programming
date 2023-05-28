#!/usr/bin/python3
"""Module containing the definition for class 'BaseGeometry'.
Public instance method: def area(self):
Raises:  Exception: with the message "area() is not implemented"
"""


class BaseGeometry:
    """A class called 'BaseGeometry' that contains an unimplemented method."""

    def area(self):
        """ Public instance method that Raises an exception when called.
        indicating that this method has not yet been implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method that validates value

        Args:
            name (str): assume name is always a string
            value (int):
                if value is not an integer:
                    Raise: TypeError exception: with the message
                    "<name> must be an integer"
                if value is less or equal to 0:
                    Raise: ValueError exception: with the message
                    "<name> must be greater than 0"
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
