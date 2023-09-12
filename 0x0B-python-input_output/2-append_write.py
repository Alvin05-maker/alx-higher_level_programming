#!/usr/bin/python3
""" Define a function that appends text to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a file.

    Args:
        filename(str): the file to append the string.
        txt(str): the string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
