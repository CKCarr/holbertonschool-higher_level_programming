#!/usr/bin/python3
""" This module writes the first class for this project the Base class """


class Base:
    """ Base class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor for Base class with optional id attribute that is
        set to None by default. If id is not None, assign the public instance.
        Args:
            id (int, optional): public instance attribute . Defaults to None.
                if ID is NULL then increment __nb_objects and assign to id
                else assign id to public instance attribute id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id