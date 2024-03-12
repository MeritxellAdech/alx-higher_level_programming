#!/usr/bin/python3

def uppercase(str):
    for i in str:
        i = ord(i) - 32 if ord(i) in range(97, 123) else ord(i)
        print("{}".format(chr(i)), end="")
    print()
