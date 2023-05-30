#!/usr/bin/python3

""" This module writes a function that creates an Object from a “JSON file”:
You must use the ''with'' statement.
Does not manage exceptions if the JSON string doesn’t represent an object.
Does not manage file permissions / exceptions. """


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.
    Returns: (object): The object created from the JSON file.
    Raises: None
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
