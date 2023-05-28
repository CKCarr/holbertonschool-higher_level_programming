#!/usr/bin/python3
""" module writes a class MyList that inherits from list """


class MyList(list):
    """ Write a class MyList that inherits from list
    with additional functionality to print a sorted
    (ascending sort) assuming that all the elements
    of the list will be of type int """
    def print_sorted(self):
        """
        Public instance method: prints the list,
        but sorted (ascending sort)
        assume that all the elements of the list will be of type int
        """
        sorted_list = sorted(self)
        print(sorted_list)
