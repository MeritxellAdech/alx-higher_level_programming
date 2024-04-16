#!/usr/bin/python3
""" Defining Geometry module """


class BaseGeometry:
    """ This is base geometry definition class"""

    def area(self):
        """ raises an exception if the area is not implemented

        Raises
            Exception error
        """
        raise Exception("area() is not implemented")
