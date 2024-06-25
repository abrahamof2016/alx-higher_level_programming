#!/usr/bin/python3
"""
module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    function for matrix division.
    arg:
        matrix: list of lists.
        div: integer or float to divide matrix.
    return:
        a new matrix.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
                )
    for lst in matrix:
        for num in lst:
            if type(num) not in [int, float] or num is None:
                raise TypeError(
                        'matrix must be a matrix'
                        '(list of lists) of integers/floats'
                        )
    """
    check if row's are equal in size.
    """
    first_row_length = len(matrix[0])
    for lst in matrix:
        if len(lst) != first_row_length:
            raise TypeError(
                    'Each row of the matrix must have the same size'
                    )
    """
    checking div.
    """
    if type(div) not in [int, float] or div is None:
        raise TypeError(
                'div must be a number'
                )
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return([list(map(lambda x: round(x / div, 2), num)) for num in matrix])
