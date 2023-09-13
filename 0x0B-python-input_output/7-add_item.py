#!/usr/bin/python3
"""import modules
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if "add_item.json" in os.listdir():
    loaded_file = list(load_from_json_file("add_item.json"))
    for i in range(1, len(sys.argv)):
        loaded_file.append(sys.argv[i])
    save_to_json_file(loaded_file, "add_item.json")
else:
    my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
