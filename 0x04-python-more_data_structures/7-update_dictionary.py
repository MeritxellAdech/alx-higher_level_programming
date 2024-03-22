#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    add or updates a key-value pair
    :param a_dict: the dict to manipulate
    :param key: the name
    :param value: key data
    :return: the new_pair or the update
    """

    if key in a_dictionary.keys():
        a_dictionary[key] = value
        a_dictionary.update()
    else:
        a_dictionary[key] = value

    return a_dictionary
