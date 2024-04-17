#!/usr/bin/python3
""" This module has a function append_write """


def append_write(filename="", text=""):
    """ appends a string to the end of a text file

    Params
        filename: str
            the path to the file
        text: str
            the content for the file
    Return
        the number of characters read
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
