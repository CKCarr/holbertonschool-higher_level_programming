#!/usr/bin/python3
""" This module Writes a class Student that defines a student.

    Public instance attributes:
        and instantiation with:
            first_name: (str) "first name of student"
            last_name: (str) "last name of student"
            age: (int)  age of a student
    Public method: 'to_json' retrieves a dictionary representation
    of a Student instance
    Returns: dictionary of a student instance """


class Student:
    """ A class to represent a Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance

        Returns:
            dict:
        Parameters:
            attrs: list, optional list of strings representing
            attribute names
                (default is None)
        """
        if attrs is None:
            return self.__dict__
        else:
            if all(isinstance(attr, str) for attr in attrs):
                parsed_dict = {}
                for attr in attrs:
                    if attr in self.__dict__:
                        parsed_dict[attr] = self.__dict__[attr]
                return parsed_dict
            else:
                return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Parameters: json : dict
        a dictionary with keys as attribute names
        and values as new attribute values
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
