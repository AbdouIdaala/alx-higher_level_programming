#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    copy = roman_string
    result = 0
    for key in list(dic):
        for i in range(len(copy)):
            if copy[i] == key:
                if copy[i] != 'I':
                    result += -1
                result += dic[key]
    return result


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CCXLVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMCDXXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
