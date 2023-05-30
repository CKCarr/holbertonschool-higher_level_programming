#!/usr/bin/python3
"""  function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object: """


def class_to_json(obj):
    """ takes a class object and returns the dictionary description.

    Args:
        obj (object): class object to be checked.

    Returns:
        object: dictionary
    """
    return obj.__dict__
