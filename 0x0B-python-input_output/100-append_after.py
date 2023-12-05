#!/usr/bin/python3
"""script for insertion of text file"""


def append_after(filename="", search_string="", new_string=""):
    """Function to insert a line of text to a file, after each line containing a spe    cific string.

    Args:
        filename (str): the file name to insert a txt
        search_string (str): The string to search.
        new_string (str): A string to write.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
