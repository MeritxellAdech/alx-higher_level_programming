#!/usr/bin/python3
""" This module loads, adds,
and saves a data from the command line into JSON file """
from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    args = []
    for i in argv:
        args.append(i)
    save(args[1:], "add_item.json")
    load("add_item.json")
