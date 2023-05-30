#!/usr/bin/python3
""" This module creates a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal’s triangle of n.

    Parameters:
    n : (int):
        The number of rows of Pascal's Triangle to generate.
    Returns: (list):
        A list of lists of integers representing Pascal's Triangle.
    """
    # If n is less than or equal to 0, return an empty list.
    if n <= 0:
        return []

    # Initialize triangle with the first row.
    triangle = [[1]]

    # Generate each row from 1 to n (not inclusive of n).
    for i in range(1, n):
        # Each row starts with 1.
        row = [1]

        # Get the last row in the triangle.
        last_row = triangle[-1]

        # Compute values in current row: adding pairs of values from last row.
        # zip()pairs each element in the last row with the one next to it.
        # sum(pair) adds each pair of values.
        # extend() adds these values to the row.
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])

        # Each row ends with 1.
        row.append(1)

        # Add the row to the triangle.
        triangle.append(row)

    # Return the completed Pascal's Triangle.
    return triangle
