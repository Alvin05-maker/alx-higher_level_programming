#!/usr/bin/python3
""" Print an integer and error to stderr"""
import sys

def safe_print_integer_err(value):
    """print an integer .

    Args:
        value(int): integer value to be printed .
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
