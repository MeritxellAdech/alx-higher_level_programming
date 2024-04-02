#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints a value if it is an integer

    :args:
        :value: the data

    return: True if value is int or False if otherwise

    """
    numeric = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        numeric = False

    return numeric
