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

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance

        Returns:
            dict:
        """
        return self.__dict__
