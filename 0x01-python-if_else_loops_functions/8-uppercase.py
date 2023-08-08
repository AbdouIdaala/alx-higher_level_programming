#!/usr/bin/python3


def uppercase(str):
    text = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            text += chr(ord(c) - 32)
    print("{}".format(text))


uppercase("best")
