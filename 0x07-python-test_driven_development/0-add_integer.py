#!/usr/bin/python3
"""
This is module for integer addition
This module has one function
The module function is add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    args:
        a = the first integer
        b = the second integer
    Return:
        sum of a and b
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b
