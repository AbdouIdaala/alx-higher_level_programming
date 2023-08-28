#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value+0))
    except TypeError:
        return False
    else:
        return True


value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

print("-------------------------")
value = '89'
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School6"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
