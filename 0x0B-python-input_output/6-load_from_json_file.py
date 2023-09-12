#!/usr/bin/python3
"""import json module
"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    with open(filename) as f:
        return json.load(f)
