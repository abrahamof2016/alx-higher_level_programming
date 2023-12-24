#!/usr/bin/python3
"""
This is module for integer addition
This module has one function, add_integer(a, b=98)

"""


def add_integer(a, b=98):
    """
    Returns a + b, an exact integer
    parameters:
    a = an integer
    b = an integer

    """
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    return a+b
