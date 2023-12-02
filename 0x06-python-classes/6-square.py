#!/usr/bin/python3
""" Module 6-square: class square """


class Square():
    """
    Square: defines a square.
    Attributes:
        size(int): size of square.
        position(int tuple): position of square.
    Method:
        __init__: initializer
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of attributes.
        Args:
            size(int): size of the square.
            position(int tuple): postion of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        getter function for private attribute size.
        Returns: size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function for private attribute size.
            Args:
            value: size value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        getter function for private attribute position
        Returns:position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter function for private attribute position
        Args:
            value: position value to be set.
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square with character #
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
