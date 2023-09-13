#!/usr/bin/python3
""" Define a class-checking function """


def is_same_class(obj, a_class):
    """ Representation of function that checks if an object is an instance of a class.

    Args:
        obj(any): The object to check.
        a_class(type) : the class to check.

    Returns:
        True - if obj is an instance of a_class.
        False - Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
