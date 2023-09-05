#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    copy = ""
    for i in range(len(text)):
        copy += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            copy += "\n\n\b"
    print(copy)
