#!/usr/bin/python3
""" This module writes the first class for this project the Base class """


class Base:
    """ Base class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor 

        Args:
            id (int, optional): public instance attribute . Defaults to None.
        """
        if id is None:
