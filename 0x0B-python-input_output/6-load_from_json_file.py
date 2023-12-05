#!/usr/bin/python3
"""Script for reading in JSON mode."""
import json


def load_from_json_file(filename):
    """Function to Read JSON file."""
    with open(filename) as f:
        return json.load(f)
