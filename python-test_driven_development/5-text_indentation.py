#!/usr/bin/python3
"""
module writes a function that prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Parameters:
    text (str): The text to be indented

    Returns:
    None

    Raises:
    TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        if i != len(lines) - 1:
            print(lines[i], end="\n")
        else:
            print(lines[i], end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
