#!/usr/bin/python3
""" Define a class """


def is_same_class(obj, a_class):
    """ Represntation of functionthat checks if an object is an instance of a class.

    Args:
        obj(any): The object to check
        a_class : the class to check
    Returns:
        True if obj is an instance of a_class.
        False Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
