#!/usr/bin/python3
"""_summary_
"""


def text_indentation(text):
    """Print a text with 2 new lines after each '.', '?' and ':'

    Args:
        text (str): the text to modify

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    copy = ""
    for i in range(len(text)):
        copy += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            copy += "\n\n\b"
    print(copy)
