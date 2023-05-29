#!/usr/bin/python3

""" This module writes a function that writes an Object to a text file,
using a JSON representation:
You must use the with statement.
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions. """


import json


def save_to_json_file(my_obj, filename):
    """ Function writes an object to text file, using it's JSON representation.

    Args:
        my_obj (object): The object to be serialized and saved to the file.
        filename (str): The name of text file to write the JSON representation.
    Returns: None
    Raises: None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
