#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        matrix2 = matrix
        for x in matrix2:
            for y in x:
                y = y * y
    return matrix2
