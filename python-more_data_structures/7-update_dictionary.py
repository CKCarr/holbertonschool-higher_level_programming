#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds
    key/value in a dictionary.
    Args:
        a_dictionary (dict): The dictionary
    """
    a_dictionary.update({key: value})
