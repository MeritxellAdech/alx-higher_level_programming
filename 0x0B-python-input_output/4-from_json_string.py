#!/usr/bin/python3
""" This module contains a function from_json_string"""
import json


def from_json_string(my_str):
    """ converts the given JSON string to an object

    Params
        my_str: JSON
            the given JSON string
    Return
        the object
    """

    return json.loads(my_str)
