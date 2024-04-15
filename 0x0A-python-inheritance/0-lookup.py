#!/usr/bin/python3

""" This module has a function that returns a list
of attributes and methods fount in an object"""


def lookup(obj):
    """
    returns a list attributes and methods of a given object

    Parameters
        obj: object
        It is the given object
    Returns
        a list containing the names of all attributes
        and methods of the object
    """
    return dir(obj)
