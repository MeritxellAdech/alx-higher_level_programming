#!/usr/bin/python3

""" Contains a class that inherits from a list"""


class MyList(list):
    """ A subclass of a list class and print the elements"""

    def print_sorted(self):
        """
        prints the list of sorted elements
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
