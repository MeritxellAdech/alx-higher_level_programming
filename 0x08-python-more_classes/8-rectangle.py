#!/usr/bin/python3

"""
This module create a rectangular class
"""


class Rectangle:
    """
    This is the definition of a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns the string representation of a rectangle"""
        shape = ""

        if self.__width == 0 or self.__height == 0:
            return shape
        for row in range(self.__height):
            shape += str(self.print_symbol) * self.__width
            if row < (self.__height - 1):
                shape += "\n"
        return shape

    def __repr__(self):
        """ returns a string representation of a rectangle new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ prints a message with a new instance is deleted """
        if Rectangle.number_of_instances == 0:
            return Rectangle.number_of_instances
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares two instances of a rectangle and
        returns the instance with the biggest area

        Parameters
            rect_1: object
            an instance of Rectangle
            rect_2: object
            an instance of Rectangle

        Return
            rect_1 if both have the same area value

        Raises
            TypeError
            if the type of either object is not object
        """
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if rect_1.area() >= rect_2.area():
                    return rect_1
                return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
