#!/usr/bin/python3
""" This module returns a boolean if the object
is 'exactly' an instance of the specified class. """


def is_same_class(obj, a_class):
    """checks if 'obj' is exactly an instance of'a_class'.

    Args:
        obj (any): The object to check
        a_class (type): The specified class to check against.

    Returns:
        bool: 'True' if obj is 'exactly' an instance of a class,
              'False' otherwise
    """
    return type(obj) is a_class
