#!/usr/bin/python3
""" This module Writes a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added.
If the file doesn’t exist, it should be created.
You must use the with statement.
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module. """


def append_write(filename="", text=""):
    """ method that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

    Args:
        filename (str, optional): The name of the text file to be read.
            filename: (Defaults to "").
        text (str, optional): The text added to the end, "appended" to file.
        text: (Defaults to "").
    Returns: (int): The number of characters added to the file.
    Raises: None
    """
    with open(filename, "a", encoding="utf8") as file:
        file.write(text)
        return len(text)
