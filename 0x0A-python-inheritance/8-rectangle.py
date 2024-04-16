#!/usr/bin/python3
""" Defining Rectangle module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents the geometry of a rectangle"""

    def __init__(self, width, height):
        """ Initialises an instance of a rectangle

        Parameters
            width: int
                width of the rectangle
            height: int
                height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
