#!/usr/bin/python3
"""Function to divide two integers and print the result"""


def safe_print_division(a, b):
    """Define the function .

    Args:
        a(int): The integer to divide .
        b(int): The divisor .
    """
    try:
        division = a/b
    except (TypeError, ZeroDivisionError):
        division = None
    finally:
        print("Inside result:{}".format(division))
        return (division)
