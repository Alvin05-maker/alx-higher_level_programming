#!/usr/bin/python3

class MyList(list):
    """ MyList class that inherits from the builtin list. """
    def __init__(self, iterable):
        """initializes MyList class"""
        super().__init__([int(item) for item in iterable])
    def print_sorted(self):
        """ Prints the list inn ascending sort order. """
        sorted_list = sorted(self)
        print(sorted_list)
