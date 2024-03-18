#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    prints all integers of a list. Integer per line

    Args:
        list: array of nubers
    """
    for i in my_list:
        print("{:d}".format(i))
