#!/usr/bin/python3
""" This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """ writes to a file

    Parameters
        filename: str
            the path of the file
        text: str
            the content to write to @filename
    Returns
        the number of characters written
    """

    written = 0
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
