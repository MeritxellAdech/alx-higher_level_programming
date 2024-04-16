#!/usr/bin/python3

""" Checking if an object is a direct/inderect instance of a class"""


def inherits_from(obj, a_class):
    """
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Parameters
        obj: is the object to check agains the class
        a_class: is the class to check against

    Return
    True if it is inherited. Otherwise, return False
    """

    return a_class in list(type(obj).__mro__)[1:]
