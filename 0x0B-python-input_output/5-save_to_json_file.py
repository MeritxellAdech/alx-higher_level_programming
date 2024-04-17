#!/usr/bin/python3
""" This module contains a function called save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file, using JSON representation
    my_obj: any
        it is any data structure
    filename: str
        the path to file
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
