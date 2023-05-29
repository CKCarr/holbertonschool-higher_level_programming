#!/usr/bin/python3
""" Module Writes a function that reads a text file (UTF8) and prints it to
stdout: """


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.
    Args:
        filename (str): The name of the text file to be read (default is "").
    Returns:
        None
    Raises:
        None: You don’t need to manage file permission or file doesn't exist
        exceptions

    """

    with open(filename, encoding="utf8") as file:
        for line in file:
            print(line, end="")
