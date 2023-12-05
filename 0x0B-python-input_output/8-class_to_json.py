#!/usr/bin/python3
"""Script that convert JSON from class."""


def class_to_json(obj):
    """Outputs object to JSON."""
    return obj.__dict__
