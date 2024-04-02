#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints x number of integers found in the list

    :args:
        :my_list: the list of values
        :x: the number of integers to print
    :return: the real number of integers printed
    """
    counted = 0

    for i in range(0, x, 1):
        try:
            print("{:d}".format(my_list[i]), end="")
            counted += 1
        except (ValueError, TypeError):
            continue
    print()
    return counted
