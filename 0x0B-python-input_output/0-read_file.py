#!/usr/bin/python3

def read_file(filename=""):
    """
    reads from a file and prints its content in the stdout

    Parameters
        filename: str
            the path to the file
    """

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
