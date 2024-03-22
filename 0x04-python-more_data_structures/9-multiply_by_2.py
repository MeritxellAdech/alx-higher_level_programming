#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    times_2a = {}
    for key in a_dictionary.keys():
        times_2a[key] = a_dictionary[key] * 2

    return times_2a
