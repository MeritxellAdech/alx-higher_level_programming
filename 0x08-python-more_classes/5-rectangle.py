#!/usr/bin/python3

"""
This module create a rectangular class
"""


class Rectangle:
    """
    This is the definition of a rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initializes an instance for a rectangle

        Parameters
        width : integer, optional
            the width of the rectangle
        height : integer, optional
            the height of the rectangle
        """

        self.width = width
        self.height = height

    def __str__(self):
        """ returns the string representation of a rectangle"""
        shape = ""

        if self.__width == 0 or self.__height == 0:
            return shape
        for row in range(self.__height):
            shape += "#" * self.__width
            if row < (self.__height - 1):
                shape += "\n"
        return shape

    def __repr__(self):
        """ returns a string representation of a rectangle new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ prints a message with a new instance is deleted """
        print("Bye rectangle...")

    @property
    def width(self):
        """ retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ assignes value to the width of the rectangle

        Parameters
        value: integer
            the value to be assigned as the width

        Raises
        TypeError
            if the value is not an integer
        ValueError
            if the value is less than 0
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ retrives the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Assignes value for the rectangle's height

        Parameters
        value: integer
            the value to be set for the height

        Raises
        TypeError
            If the height is not a number
        ValueError
            If the height is less than 0
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ returns the area of the rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimiter of the rectangle"""
        perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0

        return perimeter
