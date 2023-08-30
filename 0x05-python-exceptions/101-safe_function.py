#!/usr/bin/python3
"""Function that executes a function safely"""
import sys

def safe_function(fct, *args):
    """Define the function .

    Args:
        fct: pointer to the function to execute .
        args: arguments to fct.

    Return:
        if an error occurs - None
        else the result of call to fct
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        result = None
        print("Exception: {}".format(e), file=sys.stderr)
        return (result)
