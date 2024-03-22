#!/usr/bin/python3

def best_score(a_dictionary):
    i = 0
    found = ""
    if a_dictionary is None or a_dictionary == {}:
        return None

    for key in a_dictionary.keys():
        if a_dictionary[key] > i:
            i = a_dictionary[key]
            found = key

    return found
