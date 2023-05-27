#!/usr/bin/python3
def multiple_returns(sentence):
    """
    This function takes a string as an argument.
    If string is empty, return a tuple where first element is 0
    and second element is None.
    If string not empty, return a tuple where first element is length of string
    and the second element is first character of string.
    """
    if not sentence:
        return 0, None
    else:
        return len(sentence), sentence[0]
