#!/usr/bin/python3
"""_summary_
"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode='a', encoding='UTF-8') as f:
        num_chars = f.write(text)
        return num_chars
