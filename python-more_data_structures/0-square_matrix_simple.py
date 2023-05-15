#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create new matrix of same size as input matrix
    result = [[0 for _ in row] for row in matrix]

    # Iterate over elements in the matrix & compute the square value
    for idx_0 in range(len(matrix)):
        for idx_1 in range(len(matrix[idx_0])):
            result[idx_0][idx_1] = matrix[idx_0][idx_1] ** 2

    return (result)
