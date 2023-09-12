#!/usr/bin/python3
"""import json module
"""
import json


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    json_str = json.dumps(my_obj)
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(json_str)
