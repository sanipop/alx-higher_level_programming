#!/usr/bin/python3
"""script for writing in JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writr in JSON."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
