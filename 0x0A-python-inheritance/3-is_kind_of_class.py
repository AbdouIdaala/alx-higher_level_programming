#!/usr/bin/python3
"""_summary_
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class or type to compare against.

    Returns:
        bool: True if 'obj' is an instance of 'a_class', False otherwise.
    """
    return isinstance(obj, a_class)
