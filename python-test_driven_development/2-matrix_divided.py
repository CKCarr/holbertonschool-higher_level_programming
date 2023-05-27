#!/usr/bin/python3
""" module to write a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix should be divided by div,
    rounded to 2 decimal places.
    Args:
    matrix (lists): List of lists of integers or floats.
    div (float or int): number to divide matrix element
    raises:
    TypeError: "matrix must be matrix (list of lists) of integers/floats."
            "Each row of the matrix must have the same size"
            "div must be a number"
    ZeroDivisionError:
                div can’t be equal to 0, "division by zero"
    returns: a new matrix

        Doctest:
    # Test with a 2x2 matrix and div = 2
    >>> matrix = [[2, 4], [6, 8]]
    >>> print(matrix_divided(matrix, 2))
    [[1.0, 2.0], [3.0, 4.0]]

    # Test with a 3x3 matrix and div = 3
    >>> matrix = [[3, 6, 9], [12, 15, 18], [21, 24, 27]]
    >>> print(matrix_divided(matrix, 3))
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

    # Test with non-rectangular matrix
    >>> matrix = [[1, 2], [3, 4, 5]]
    >>> try:
    ...     print(matrix_divided(matrix, 2))
    ... except TypeError as e:
    ...     print(e)
    Each row of the matrix must have the same size

    # Test with non-numeric elements in matrix
    >>> matrix = [[1, 2], [3, '4']]
    >>> try:
    ...     print(matrix_divided(matrix, 2))
    ... except TypeError as e:
    ...     print(e)
    matrix must be a matrix (list of lists) of integers/floats
    """
    not_list = "matrix must be a matrix (list of lists) of integers/floats"
    size = "Each row of the matrix must have the same size"
    num = "div must be a number"
    zero = "division by zero"
    # matrix must be a list of lists
    if not isinstance(matrix, list):
        raise TypeError(not_list)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(not_list)

    # all elements in the matrix are either int or float
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(not_list)

    # all row in the matrix have the same length (matrix is rectangular)
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(size)

    # the div are should be a number either int or float
    if not isinstance(div, (int, float)):
        raise TypeError(num)

    # the div arg cannot be zero, div by zero undefined
    if div == 0:
        raise ZeroDivisionError(zero)

    # After validating input we perform division
    # For each row in the matrix, we create a new row.
    # Each element in new row from old row divided by div, rounded 2 decimals
    # We use the round function to perform the rounding.
    # Finally, we return the new matrix.
    return [[round(elem / div, 2) for elem in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
