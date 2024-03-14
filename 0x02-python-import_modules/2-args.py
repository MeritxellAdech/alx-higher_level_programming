#!/usr/bin/python3

from sys import argv


def dynamic():
    args = len(argv) - 1
    res = "argument" if args == 1 else "arguments"
    sign = "." if args == 0 else ":"
    print("{} {}{}".format(args, res, sign))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    dynamic()
