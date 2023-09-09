#!/usr/bin/python3
"""
DEFINE A FUNCTION THAT PRINTS SQUARE
Args:
    size(int).
"""
def print_square(size):
    """
    Representation of a function that prints square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square using nested loops
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()  # Move to the next line after each row

