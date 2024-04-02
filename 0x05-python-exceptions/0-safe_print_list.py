#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints the numbers found in the given list

    :args:
     :mylist: is the given list
     :x: the number of items to be printed

    Return: the number of numbers found
    """
    counted = 0
    try:
        for num in my_list:
            if counted < x:
                print("{:d}".format(num), end="")
                counted += 1
        print()
    except IndexError:
        print()
    return counted
