#!/usr/bin/python3
""" This module has the to_json_string function """
import json


def to_json_string(my_obj):
    """ converts a given object to JSON
    Params
        my_obj: any
            the data to be converted to JSON
    Return
        the data in JSON format
    """

    return json.dumps(my_obj)
