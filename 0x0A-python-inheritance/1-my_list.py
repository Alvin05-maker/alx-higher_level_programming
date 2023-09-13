#!/usr/bin/python3
""" Define a class MyList."""


class MyList(list):
    """ Return a list in ascending sort manner"""

    def print_sorted(self):
        """ Prints the list in ascending sort."""
        sorted_self = sorted(self)
        print(sorted_self)
