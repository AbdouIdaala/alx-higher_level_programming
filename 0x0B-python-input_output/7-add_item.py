#!/usr/bin/python3
"""import modules
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# writes an Object to a text file, using a JSON representation
# save_to_json_file(my_obj, filename)
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
# creates an Object from a “JSON file”
# load_from_json_file(filename)


my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, "add_item.json")