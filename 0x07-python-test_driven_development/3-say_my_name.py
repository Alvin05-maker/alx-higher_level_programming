#!/usr/bin/python3
"""
Define a function that prints the name .
Args:
    first_name(str) and last_name(str).
"""
def say_my_name(first_name, last_name=""):
    """
    Returns the name .
    """
    if not isinstance (first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
