#!/usr/bin/python3
# 6-from_json_string.py
"""String that convert from JSON to object"""
import json


def from_json_string(my_str):
    """Function converts JSON to py obj."""
    return json.loads(my_str)
