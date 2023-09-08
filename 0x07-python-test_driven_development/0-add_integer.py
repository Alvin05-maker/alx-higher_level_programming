#!/usr/bin/python3
"""
Define a function that adds two integers.
Args:
    int(a) and int(b).
"""
def add_integer(a, b=98):
    """
    Return:Return the sum of the two integers(a + b).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance((a, b), float):
        a = int(a)
        b = int(b)
    return (int(a+b))
