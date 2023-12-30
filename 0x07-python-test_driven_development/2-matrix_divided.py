#!/usr/bin/python3
""" module for matrix division """


def matrix_divided(matrix, div):
    """
    computes matrix division
    arguments:
        matrix: list of list
        div: an integer or float
    return:
        a new matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    matrix2 = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = [[round(j/div, 2) for j in i] for i in matrix]
    return matrix2
