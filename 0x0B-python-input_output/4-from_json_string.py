#!/usr/bin/python3
"""Define a function that returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Return the object string form JSON.

    Args:
        my_str(str).

    Returns:
        The objects string.
    """
    return json.loads(my_str)
