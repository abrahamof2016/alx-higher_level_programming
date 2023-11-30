#!/usr/bin/python3
""" Module contains: class Square """


class Square:
    """
    Square: define a square
    Attributes:
        size: size of square
    Method:
        __init__: init of size attribute for each instance
    """
    def __init__(self, size):
        """
        Initialization of attributes for all instances
        Args:
            size: size of the square
        """
        self.__size = size
