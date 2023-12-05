#!/usr/bin/python3
"""Script that have a string converted to JSON."""
import json


def to_json_string(my_obj):
    """A Function that convert an object to JSON."""
    return json.dumps(my_obj)
