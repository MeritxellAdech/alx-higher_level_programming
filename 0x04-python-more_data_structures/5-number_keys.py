#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    counts the keys available in a dict

    Args:
        a_dictionary: the dictionary to check for keys

    Return:
        the number of keys counted
    """
    i = 0
    for key in a_dictionary.keys():
        i += 1
    return i
