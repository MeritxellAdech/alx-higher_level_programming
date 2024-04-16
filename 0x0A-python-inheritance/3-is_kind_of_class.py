#!/usr/bin/python3

""" Checking if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class

    Parameters
        obj: is the object to check agains the class
        a_class: is the class to check against

    Return
    True if the object is an instance of the given class
    Otherwise, return False
    """

    return isinstance(obj, a_class)
