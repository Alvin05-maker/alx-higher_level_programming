#!/usr/bin/python3
""" Define a subclass-checking function """


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a subclass.

    Args:
        obj(any): The object to check.
        a_class(type) : the class to check.

    Returns:
        True - if obj is an instance of a subclass of class a_class.
        False - Otherwise.
    """
    if issubclass(type(obj), a_class) and  type(obj) != a_class:
        return True
    return False
