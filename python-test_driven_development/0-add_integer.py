<<<<<<< HEAD
#!/usr/bin/python3
"""This module writes a function that adds 2 integers"""

def add_integer(a, b=98):
    """
    Function to add two numbers together.
    :param a: first number must be integer or float.
    :param b: second number must be an int or float (default 98).
    :return: the sum of a and b as an integer.
    :raises: TypeError: If either a or b is not an int or float.

        Doctest:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    a must be an integer
    """
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
=======
#!/usr/bin/python3
"""This module writes a function that adds 2 integers"""


def add_integer(a, b=98):
    """
    Function to add two numbers together.
    :param a: first number must be integer or float.
    :param b: second number must be an int or float (default 98).
    :return: the sum of a and b as an integer.
    :raises: TypeError: If either a or b is not an int or float.

        Doctest:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
>>>>>>> a41fa0acb26bccad7a617404b5dc2644bba09de5
