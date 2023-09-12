#!/usr/bin/python3
""" Defines a function that reads a textfile and prints it to stdout."""


def read_file(filename=""):
    """Represent a read file function ."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
