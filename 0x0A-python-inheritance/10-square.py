#!/usr/bin/python3
""" Defining Square module """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Represents the geometry of a square"""

    def __init__(self, width, height):
        """ Initialises an instance of a square

        Parameters
            width: int
                width of the square
            height: int
                height of the square
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of a square"""
        return self.__width * self.__height
