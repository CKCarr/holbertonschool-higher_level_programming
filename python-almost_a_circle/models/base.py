#!/usr/bin/python3
""" This module writes the first class for this project the Base class """

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that Returns: the JSON string representation
        of a list of dictionaries.
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method writes the JSON representation of a string to a file.

        Args:
            list_objs (list): list of instances who inherits from
            Base - examples: List of Rectangle instances
            or List of Square instances.
        """
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        # convert list objects to list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        # convert list dictionaries to json string
        json_str = cls.to_json_string(list_dicts)
        # write the JSON string to a file
        with open(filename, "w") as file:
            file.write(json_str)
