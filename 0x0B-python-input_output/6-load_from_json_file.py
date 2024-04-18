#!/usr/bin/python3
""" This module contains load_from_json_file function """
import json


def load_from_json_file(filename):
    """ create an object from a JSON file

    filename: str
        the path to the file
    Return
        the object
    """

    obj = None
    with open(filename, "r", encoding="utf-8") as file:
        obj = json.loads(file.read())

    return obj
