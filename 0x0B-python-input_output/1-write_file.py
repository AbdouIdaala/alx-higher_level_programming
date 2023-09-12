#!/usr/bin/python3
"""_summary_
"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode='w', encoding='UTF-8') as f:
        num_chars = f.write(text)
        return num_chars
