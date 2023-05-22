#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
    first_name (str): The first name
    last_name (str, optional): The last name. Defaults to "".

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Doctest:

    >>> say_my_name("John", "Doe")
    My name is John Doe

    >>> say_my_name("John")
    My name is John

    >>> say_my_name(123, "Doe")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

    >>> say_my_name("John", 123)
    Traceback (most recent call last):
    ...
    TypeError: last_name must be a string

    >>> say_my_name()
    Traceback (most recent call last):
    ...
TypeError: say_my_name() missing 1 required positional argument: 'first_name'

    >>> say_my_name('Joe', Dirt)
    Traceback (most recent call last):
    ...
    NameError: name 'Dirt' is not defined
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
