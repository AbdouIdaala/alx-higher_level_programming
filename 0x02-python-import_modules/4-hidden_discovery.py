#!/usr/bin/python3
def helper():
    with open("./hidden_4.pyc", 'rb') as f:
        return f.read()


if __name__ == "__main__":
    print(helper())
