#!/usr/bin/python3
""" This module has a function the reads from a file"""


def read_file(filename=""):
    """
    reads from a file and prints its content in the stdout

    Parameters
        filename: str
            the path to the file
    """

    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
