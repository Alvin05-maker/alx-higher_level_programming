#!/usr/bin/python3
""" Define a function that writes text to a file."""


def write_file(filename="", text=""):
    """Writes a text to a file.

    Args:
        filename(str): name of file to write to.
        text(str): text to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
