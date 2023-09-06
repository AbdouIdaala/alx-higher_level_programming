#!/usr/bin/python3
"""_summary_
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>

    Args:
        first_name (str): mandatory
        last_name (str, optional): Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
