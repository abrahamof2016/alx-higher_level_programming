#!/usr/bin/python3
""" Define a class Rectangle """


class Rectangle:
    """
    Rectangle: defines a class rectangle
    Attributes:
        width: width of rectangle
        height: height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an attributes
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def height(self):
        """
        getter method for height attribute
        Return: height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute
        Args: value which is the new width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        getter method for width attribute
        Return: width of a rectangle
        """
        return self.__width

    @height.setter
    def width(self, value):
        """
        setter method for width attribute
        Args: value (which is the new width to be set)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
