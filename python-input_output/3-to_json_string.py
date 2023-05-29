#!/usr/bin/python3
""" This module writes a function that returns the JSON representation
of an object (string):
You don’t need to manage exceptions if the object can’t be serialized."""


import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string):

    Args:
        my_obj (onject): The object to be serialized to JSON.
    Returns: (str): The JSON representation of the object as a string.
    Raises: None
    """
    return json.dumps(my_obj)
