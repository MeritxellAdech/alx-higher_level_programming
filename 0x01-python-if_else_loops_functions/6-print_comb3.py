#!/usr/bin/python3

for first in range(10):
    for last in range(10):
        if first > last or first == last:
            continue
        if first == 8 and last == 9:
            print("{}{}".format(first, last))
            break
        print("{}{}".format(first, last), end=", ")
