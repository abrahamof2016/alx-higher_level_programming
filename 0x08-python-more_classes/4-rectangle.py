#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """
    Defines a ectangle
    Attributes:
        width: width of rectangle
        height: height of rectangle
    Methods:
        __init__: Initializes attributes
        area: returns rectangle area
        perimeter: returns perimeter of rectangle
        __str__: prints rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes attributes
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter method to retrive width variable
        Return: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method to set width of variable
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method to retrive height of variable
        Return: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method to set new height of rectangle
        Args:
            value: a new height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """
        finds an area of rectangle
        Return:
            area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        finds perimeter of rectangle
        Return:
            perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2*self.__height) + (2*self.__width)

    def __str__(self):
        """
        prints rectangle with character #
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width
        return rectangle

    def __repr__(self):
        """
        returns string representation of rectangle
        representation should be recreated into a new instance using eval
        """
        rectangle = ''
        if self.__width is 0 or self.__height is 0:
            return rectangle
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle
