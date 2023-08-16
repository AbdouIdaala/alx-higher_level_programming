#!/usr/bin/python3
def dictionary():
    roman_dict = [
        {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9
        },
        {
            "X": 10,
            "XX": 20,
            "XXX": 30,
            "XL": 40,
            "L": 50,
            "LX": 60,
            "LXX": 70,
            "LXXX": 80,
            "XC": 90
        },
        {
            "C": 100,
            "CC": 200,
            "CCC": 300,
            "CD": 400,
            "D": 500,
            "DC": 600,
            "DCC": 700,
            "DCCC": 800,
            "CM": 900
        },
        {
            "M": 1000,
            "MM": 2000,
            "MMM": 3000
        }
    ]
    return roman_dict


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    reference = dictionary()
    result = 0
    for dic in reference:
        for key, value in dic.items():
            if key == roman_string:
                return value
            else:
                for c in roman_string:
                    if c == key:
                        result += value
    return result
