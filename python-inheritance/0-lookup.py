#!/usr/bin/python3
""" module with function that returns the list of
    available attributes and methods of an object."""


def lookup(obj):
    """ function that returns the list of available attributes and methods of an object.
    :param obj: (object) The object to inspect.   :return: list: A list containing the names of attributes and methods. """
    attr_and_meth = dir(obj)
    return attr_and_meth


if __name__ == "__main__":
    pass
