#!/usr/bin/python3
"""
This module Writes a function that returns True if the object is an
instance of a class that inherited (directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ function checks if object is an instance of a class or derived class of
    the specified class.

    Args:
        obj (any): The object to be check.
        a_class (type): The Class given to check against.
    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
