#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ function that prints a dictionary by ordered keys.
    Args:
        a_dictionary (dict): the dictionary
    """
    # sorted returns a list of keys sorted in ascending order.
    sorted_keys = sorted(a_dictionary)
    # iterate through sorted dict
    for key in sorted_keys:
        # print key : value pair
        print(key + ":", a_dictionary[key])
