#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        if key in a_dictionary:
            print("{}: {}".format(key, a_dictionary.get(key)))
