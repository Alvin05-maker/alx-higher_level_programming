#!/usr/bin/python3
"""Define a function thatinds attributes and methods of a given object."""


def lookup(obj):
    """ Returns all available attributes and methods of an object."""
    return [attribute for attribute in dir(obj)]
