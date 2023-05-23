#!/usr/bin/python3
""" This module Writes a function that prints
    a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character '#'

    Parameters:
    size (int): The size length of the square

    Returns:
    None

    Raises:
    TypeError: If size is not an integer
    ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
