#!/usr/bin/python3
"""_summary_
"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    return issubclass(type(obj), a_class) or isinstance(obj, a_class)
