#!/usr/bin/python3

def print_last_digit(number):
    remainder = number % 10 if number > 0 else (-number) % 10
    print(remainder, end="")
    return remainder
