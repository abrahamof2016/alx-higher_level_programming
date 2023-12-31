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
    if not all(isinstance(item, list) for item in matrix):
        raise TypeError(
                "matrix must be a matrix(list of list)of integers/floats"
                )
    """ check if the matrix has equal row size """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    for i in range(len(matrix)-1):
        if not len(matrix[i]) == len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")
    matrix2 = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = [[round(j/div, 2) for j in i] for i in matrix]
    return matrix2
