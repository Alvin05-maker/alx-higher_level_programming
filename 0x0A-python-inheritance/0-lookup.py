#!/usr/bin/python3

def lookup(obj):
    """ Returns all available attributes and methods of an object."""
    return [attribute for attribute in dir(obj)]
