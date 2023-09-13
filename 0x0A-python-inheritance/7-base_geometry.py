#!/usr/bin/python3
"""Define a BaseGeometry class"""


class BaseGeometry:
    """Representation of the class."""
    def area(self):
        """ Not yet implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Validates integers."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
