#!/usr/bin/python3
""" This Module Writes a function that writes a string to a text file (UTF8)
and returns the number of characters written.
You must use the with statement.
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module """


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (str, optional): The name of the text file to be read.
            filename: (Defaults to "").
        text (str, optional): The text to be written to the file.
            text: (Defaults to "").
    Returns: (int): The number of characters written to file.
    Raises: None """
    with open(filename, "w", encoding="utf8") as file:
        file.write(text)
        return len(text)
