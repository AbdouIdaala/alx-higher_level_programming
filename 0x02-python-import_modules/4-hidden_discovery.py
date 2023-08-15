#!/usr/bin/python3
if __name__ == "__main__":
    file = open("./hidden_4.pyc", 'rb').read()
    print(str(file, encoding='latin-1'))
