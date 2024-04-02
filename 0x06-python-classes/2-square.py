#!/usr/bin/python3

"""
Module definition for the Square class
"""


class Square:
    """
    defines a square
    """

    def __init__(self, size=0):
        """
        initializes the values given to the class

        :args:
            :size: the size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >=0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
