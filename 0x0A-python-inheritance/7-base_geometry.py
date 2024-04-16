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

    def integer_validator(self, name, value):
        """ Ensure that the value assigned to value is valid

        Parameters
            name: str
                any given shape name
            value: int
                any given integer

        Raises
            ValueError: when the assigned value is <= 0
            TypeError: when the type is not int
        """

        if type(value) is int:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
