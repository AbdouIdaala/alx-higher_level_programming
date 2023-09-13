#!/usr/bin/python3
"""_summary_
"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode='r', encoding='UTF-8') as f:
        print(f.readlines())
