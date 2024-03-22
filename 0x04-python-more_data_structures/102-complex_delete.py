#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    deletes a key from in a dictionary

    :param a_dictionary: the dictionary
    :param value: the value whose key is to be deleted
    :return: the dictionary
    """
    rest = {}
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            del key
            continue
        rest[key] = a_dictionary[key]

    return rest
