#!/usr/bin/python3
""" Define string to json function ."""
import json


def to_json_string(my_obj):
    """JSON representation of an object.

    Args:
        my_obj(str): my object string.

    Returns:
            The json representation of an object(string).
    """
    return json.dumps(my_obj)
