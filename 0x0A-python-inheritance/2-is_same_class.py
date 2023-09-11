#!/usr/bin/python3
"""_summary_
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class or type to compare against.

    Returns:
        bool: True if 'obj' is an instance of 'a_class', False otherwise.
    """
    if a_class is not object:
        return isinstance(obj, a_class)
