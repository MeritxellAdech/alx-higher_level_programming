#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
     deletes a key in a dictionary
     :param a_dictionary: the dictionary to manipulate
     :param key: is the key to be deleted
     :return: the updated dictionary
    """

    if key in a_dictionary.keys():
        del a_dictionary[key]

    return a_dictionary
