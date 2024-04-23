#!/usr/bin/python3
"""   """


def add_integer(a, b=98):
    """ adds two integers

    Params
        a: first number
        b: second number
    Returns
        the sum total
    Raises
        TypeError if the number is not a number
    """

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
