#!/usr/bin/python3
from sys import argv


def infinite():
    sum = 0
    for n in range(1, len(argv)):
        sum += int(argv[n])
    print(sum)


if __name__ == "__main__":
    infinite()
