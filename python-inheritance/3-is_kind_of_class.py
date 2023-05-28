#!/usr/bin/python3
""" This module returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """ This function checks if an object is an instance of the class,
    or a derived class of the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to check against.
    Returns:
        bool: True if obj is an instance of the class or a subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
