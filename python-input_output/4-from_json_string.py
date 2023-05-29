#!/usr/bin/python3

""" This module writes a function that returns an object
(Python data structure) represented by a JSON string:
does not manage exceptions if the JSON string doesn’t represent an object."""


import json


def from_json_string(my_str):
    """ Function returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to an object.
    Returns: (object): The Python Data Structure represented by the string.
    Raises: None
    """
    return json.loads(my_str)
