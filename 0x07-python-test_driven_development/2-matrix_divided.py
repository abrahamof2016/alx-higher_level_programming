#!/usr/bin/python3
""" Module for matrix division """


def matrix_divided(matrix, div):
    """
    computes matrix division
    arg:
        matrix: list of lists
        div: an integer or float
    return:
         a new matrix
    """
    """ check if the matrix is list of list """
    if isinstance(matrix, list):
        for lst in matrix:
            if isinstance(lst, list):
                for num in lst:
                    if type(num) not in [int, float] or num is None:
                        raise TypeError(
                                'matrix must be a matrix'
                                '(list of lists)of integers/floats'
                                )
            if not isinstance(lst, list):
                raise TypeError(
                        'matrix must be a matrix'
                        '(list of lists)of integers/floats'
                        )
    if not isinstance(matrix, list):
        raise TypeError(
                'matrix must be a matrix (list of lists)of integers/floats'
                )
    """ check if the matrix has equal row size """
    for i in range(len(matrix)-1):
        if not len(matrix[i]) == len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")
    """ check for the values fo div """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = [[round(j/div, 2) for j in i] for i in matrix]
    return matrix2
